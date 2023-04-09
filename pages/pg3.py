import plotly.express as px
import dash
from dash import html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from utils.Data import Realtime

dash.register_page(__name__, name='Predictive Analysis')

# Define the layout for the overview page
Overview_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [dcc.Graph(figure=Realtime.summary_plot())
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
                                figure=Realtime.flow_plot()
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
                                figure=Realtime.total_count_plot()
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
