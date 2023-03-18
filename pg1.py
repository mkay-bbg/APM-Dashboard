import numpy as np
import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
from datetime import datetime
import dash_bootstrap_components as dbc


# '/' is home page
dash.register_page(__name__, path='/', name='Overview and Summary')


df = pd.read_csv('data_v1.1.csv')

# Data manipulation
df['datetime'] = pd.to_datetime(df['datetime'])
df["time"] = df['datetime'].dt.time
df["date"] = df['datetime'].dt.date
df['Net Change'] = df['ppl_in'] - df['ppl_out']


Capacity_per_car = 76
df['Ppl Onboard'] = df['Net Change'].cumsum()
df['Occupancy Rate'] = df['Ppl Onboard'] / Capacity_per_car


df = df.groupby(['datetime', 'date', 'time', 'Car', 'door',
                'ppl_out', 'ppl_in', 'Net Change', 'Ppl Onboard', 'Occupancy Rate']).count()
df.reset_index(inplace=True)

# Calculate the key figures
occupancy_rate = float(df['Occupancy Rate'].tail(1))
occupancy_rate_percent = "{:.2%}".format(occupancy_rate)
ppl_onboard = int(df['Ppl Onboard'].tail(1))
traffic = int(df['ppl_in'].sum())
average_traffic = float((df['ppl_in'].mean()))

# Generate the lower level dataframes
dfc1 = df[df['Car'] == 1]
dfc2 = df[df['Car'] == 2]
dfc1d1 = dfc1[dfc1['door'] == 1]
dfc1d2 = dfc1[dfc1['door'] == 2]
dfc2d1 = dfc2[dfc2['door'] == 1]
dfc2d2 = dfc2[dfc2['door'] == 2]

# Define the layout for the overview tab
# Overview_content = dbc.Card(
#     dbc.CardBody(
#         [
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [dcc.Graph(figure=px.line(
#                             df, x=df['datetime'], y=df['Net Change'], title='Net Change'))
#                          ], width=12
#                     )
#                 ]
#             ),
#         ]
#     ),
#     className="mt-3",
# )

Overview_content = html.Div(
    [
        dbc.Col(
            dbc.CardGroup(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Occupancy Rate",
                                        className="card-title"),
                                html.P(occupancy_rate_percent
                                       ),
                            ]
                        )
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Passenger Volume",
                                        className="card-title"),
                                html.P(
                                    traffic
                                ),
                            ]
                        )
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("People Onboard",
                                        className="card-title"),
                                html.P(
                                    ppl_onboard
                                ),
                            ]
                        )
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Avg. Passenger Flow",
                                        className="card-title"),
                                html.P(
                                    f'{average_traffic:.2f}'
                                )
                            ]
                        )
                    )
                ]
            ),
            width=12),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [dcc.Graph(figure=px.line(
                                        df, x=df['datetime'], y=df['Net Change'], title='Net Change'))
                                     ], width=12
                                )
                            ]
                        )
                    ]
                )
            ),
        width=12)
    ]
)


# Define the layout for the performance tab
Performance_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(figure=px.line(
                                dfc1, x='datetime', y=dfc1.columns[5:], title='People in and out over time')),
                            dcc.Graph(figure=px.line(
                                dfc1, x=dfc1['time'], y=dfc1.columns[5:], title='Average people inflow and outflow over time of every minute')),
                            dcc.Graph(figure=px.line(
                                dfc1, x=dfc1['datetime'], y=dfc1['Net Change'], title='Net Change'))
                        ], width=12
                    )
                ]
            ),
        ]
    ),
    className="mt-3",
)
# Define the layout for the suggestion tab
Suggestion_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(figure=px.line(
                                dfc2, x='datetime', y=dfc2.columns[5:], title='People in and out over time')),
                            dcc.Graph(figure=px.line(
                                dfc2, x=dfc2['time'], y=dfc2.columns[5:], title='Average people inflow and outflow over time of every minute')),
                            dcc.Graph(figure=px.line(
                                dfc2, x=dfc2['datetime'], y=dfc2['Net Change'], title='Net Change'))
                        ], width=12
                    )
                ]
            ),
        ]
    ),
    className="mt-3",
)

# Define the app layout
layout = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Overview",
                        tab_id="tab-overview"),
                dbc.Tab(label="Performance",
                        tab_id="tab-performance"),
                dbc.Tab(label="Suggestion",
                        tab_id="tab-suggestion")
            ],
            id="tabs-pg1",
            active_tab="tab-overview",
        ),
        html.Div(id="content-pg1")
    ]
)

# Define the callback for switching tabs


@callback(Output("content-pg1", "children"), [Input("tabs-pg1", "active_tab")])
def switch_tab(at):
    if at == "tab-overview":
        return Overview_content
    elif at == "tab-performance":
        return Performance_content
    elif at == "tab-suggestion":
        return Suggestion_content
