import plotly.express as px
import dash
from dash import html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from utils.Data import Realtime, KPI, C1_Subseries, C2_Subseries


# '/' is home page
dash.register_page(__name__, path='/', name='Overview and Summary')

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
                                html.P(KPI.occupancy_rate_percent()
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
                                    KPI.traffic()
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
                                    KPI.ppl_onboard()
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
                                    f'{KPI.average_traffic():.2f}'
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
                                    [dcc.Graph(figure=Realtime.summary_plot())
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


# # Define the layout for the trainflow tab
# Performance_content = dbc.Card(
#     dbc.CardBody(
#         [
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [
#                             dcc.Graph(figure=C1_Subseries.flow_plot()),
#                             dcc.Graph(figure=C1_Subseries.min_subplot())
#                         ], width=12
#                     )
#                 ]
#             ),
#         ]
#     ),
#     className="mt-3",
# )

Performance_content = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id="C1-item-content"),
                    title="Car 1",
                    item_id="C1-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C1D1-item-content"),
                    title="Door 1",
                    item_id="C1D1-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C1D2-item-content"),
                    title="Door 2",
                    item_id="C1D2-item",
                )
            ],
            id="accordion-C1-pg2",
            active_item="C1-item",
            always_open=True,
        )
    ]
)

accordion_C1_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C1_Subseries.flow_plot()),
                                                    dcc.Graph(figure=C1_Subseries.min_subplot())
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

accordion_C1D1_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C1_Subseries.d1_flow_plot()),
                                                    dcc.Graph(figure=C1_Subseries.d1_min_subplot())
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

accordion_C1D2_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C1_Subseries.d2_flow_plot()),
                                                    dcc.Graph(figure=C1_Subseries.d2_min_subplot())                                                   
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

# Define the layout for the suggestion tab
Suggestion_content = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id="C2-item-content"),
                    title="Car 2",
                    item_id="C2-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C2D1-item-content"),
                    title="Door 1",
                    item_id="C2D1-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C2D2-item-content"),
                    title="Door 2",
                    item_id="C2D2-item",
                )
            ],
            id="accordion-C2-pg2",
            active_item="C2-item",
            always_open=True,
        )
    ]
)

accordion_C2_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C2_Subseries.flow_plot()),
                                                    dcc.Graph(figure=C2_Subseries.min_subplot())
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

accordion_C2D1_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C2_Subseries.d1_flow_plot()),
                                                    dcc.Graph(figure=C2_Subseries.d1_min_subplot())
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

accordion_C2D2_content = [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(figure=C2_Subseries.d2_flow_plot()),
                                                    dcc.Graph(figure=C2_Subseries.d2_min_subplot())
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

# Define the app layout
layout = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Overview & KPIs",
                        tab_id="tab-overview"),
                dbc.Tab(label="Train 1 flow",
                        tab_id="tab-performance"),
                dbc.Tab(label="Train 2 flow",
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
