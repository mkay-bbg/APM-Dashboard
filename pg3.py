import numpy as np
import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
from datetime import datetime
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Predictive Analysis')

df = pd.read_csv('data_v1.1.csv')

df['datetime'] = pd.to_datetime(df['datetime'])
df["time"] = df['datetime'].dt.time
df["date"] = df['datetime'].dt.date
df['Net Change'] = df['ppl_in'] - df['ppl_out']
df = df.groupby(['datetime', 'date', 'time', 'Car', 'door',
                'ppl_out', 'ppl_in', 'Net Change']).count()
df.reset_index(inplace=True)

dfc1 = df[df['Car'] == 1]
dfc2 = df[df['Car'] == 2]
dfc1d1 = dfc1[dfc1['door'] == 1]
dfc1d2 = dfc1[dfc1['door'] == 2]
dfc2d1 = dfc2[dfc2['door'] == 1]
dfc2d2 = dfc2[dfc2['door'] == 2]

# Define the layout for the overview page
Overview_content = dbc.Card(
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
            ),
        ]
    ),
    className="mt-3",
)

# Define the layout for the car-1 data page
Car_1_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id='entering-exiting-graph',
                                figure=px.line(df, x='datetime', y=[
                                    'ppl_in', 'ppl_out'], title='People Entering and Exiting')
                            )
                        ], width=12
                    )
                ]
            ),
        ]
    ),
    className="mt-3",
)
# Define the layout for the car-2 data page
Car_2_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id='total-count-graph',
                                figure=px.line(df, x='datetime', y='Net Change',
                                               title='Total People Count')
                            )
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
                dbc.Tab(label="Car 1 Data",
                        tab_id="tab-car-1"),
                dbc.Tab(label="Car 2 Data",
                        tab_id="tab-car-2")
            ],
            id="tabs-pg3",
            active_tab="tab-overview",
        ),
        html.Div(id="content-pg3")
    ]
)

# Define the callback for switching tabs
@callback(Output("content-pg3", "children"), [Input("tabs-pg3", "active_tab")])
def switch_tab(at):
    if at == "tab-overview":
        return Overview_content
    elif at == "tab-car-1":
        return Car_1_content
    elif at == "tab-car-2":
        return Car_2_content
