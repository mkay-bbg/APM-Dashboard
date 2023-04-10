import dash
from dash import html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from utils.Data import Realtime, C1_Subseries, C2_Subseries, Analysis

dash.register_page(__name__, name='Data Analytics')

# df = pd.read_csv('data_v1.1.csv')

# df['datetime'] = pd.to_datetime(df['datetime'])
# df["time"] = df['datetime'].dt.time
# df["date"] = df['datetime'].dt.date
# df['Net Change'] = df['ppl_in'] - df['ppl_out']
# df = df.groupby(['datetime', 'date', 'time', 'Car', 'door',
#                 'ppl_out', 'ppl_in', 'Net Change']).count()
# df.reset_index(inplace=True)

# dfc1 = df[df['Car'] == 1]
# dfc1.reset_index(inplace=True)
# dfc2 = df[df['Car'] == 2]
# dfc2.reset_index(inplace=True)
# dfc1d1 = dfc1[dfc1['door'] == 1]
# dfc1d1.reset_index(inplace=True)
# dfc1d2 = dfc1[dfc1['door'] == 2]
# dfc1d2.reset_index(inplace=True)
# dfc2d1 = dfc2[dfc2['door'] == 1]
# dfc2d1.reset_index(inplace=True)
# dfc2d2 = dfc2[dfc2['door'] == 2]
# dfc2d2.reset_index(inplace=True)

# Define the layout for the overview tab

Overview_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [dcc.Graph(figure=Analysis.hourly_analysis())
                         ], width=12
                    )
                ]
            ),
        ]
    ),
    className="mt-3",
)

# Define the layout for the car-1 data tab

Car_1_content = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id="C1-item-content"),
                    title="15 Minutes moving average",
                    item_id="C1-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C1D1-item-content"),
                    title="1 Hour moving average",
                    item_id="C1D1-item",
                ),
                dbc.AccordionItem(
                    html.Div(id="C1D2-item-content"),
                    title="1 Day moving average",
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
                                                    dcc.Graph(figure=Analysis.MA()["15min"]),
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
                                                    dcc.Graph(figure=Analysis.MA()["H"])
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
                                                    dcc.Graph(figure=Analysis.MA()["D"])
                                                ], width=12
                                            )
                                        ]
                                    ),
                                ]
                            ),
                            className="mt-3",
                        )
                    ]

# Define the layout for the car-2 data tab
Car_2_content = html.Div(
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
                dbc.Tab(label="Daily level analysis",
                        tab_id="tab-overview"),
                dbc.Tab(label="Moving average of people flow",
                        tab_id="tab-car-1"),
                dbc.Tab(label="Car 2 Data",
                        tab_id="tab-car-2")
            ],
            id="tabs-pg2",
            active_tab="tab-overview",
        ),
        html.Div(id="content-pg2")
    ]
)

# Define the callback for switching tabs
@callback(Output("content-pg2", "children"), [Input("tabs-pg2", "active_tab")])
def switch_tab(tab):
    if tab == "tab-overview":
        return Overview_content
    elif tab == "tab-car-1":
        return Car_1_content
    elif tab == "tab-car-2":
        return Car_2_content

# Define the callback for C1 item in Car 1 tab accordion  
@callback(
    Output("C1-item-content", "children"),
    [Input("accordion-C1-pg2", "active_item")],
)
def change_item_C1(item):
    if "C1-item" in item:
        return accordion_C1_content

# Define the callback for C1D1 item in Car 1 tab accordion  
@callback(
    Output("C1D1-item-content", "children"),
    [Input("accordion-C1-pg2", "active_item")],
)
def change_item_C1D1(item):
    if "C1D1-item" in item:
        return accordion_C1D1_content

# Define the callback for C1D2 item in Car 1 tab accordion 
@callback(
    Output("C1D2-item-content", "children"),
    [Input("accordion-C1-pg2", "active_item")],
)
def change_item_C1D2(item):
    if "C1D2-item" in item:
        return accordion_C1D2_content

# Define the callback for C2 item in Car 2 tab accordion 
@callback(
    Output("C2-item-content", "children"),
    [Input("accordion-C2-pg2", "active_item")],
)
def change_item_C2(item):
    if "C2-item" in item:
        return accordion_C2_content

# Define the callback for C2D1 item in Car 2 tab accordion 
@callback(
    Output("C2D1-item-content", "children"),
    [Input("accordion-C2-pg2", "active_item")],
)
def change_item_C2D1(item):
    if "C2D1-item" in item:
        return accordion_C2D1_content

# Define the callback for C2D2 item in Car 2 tab accordion 
@callback(
    Output("C2D2-item-content", "children"),
    [Input("accordion-C2-pg2", "active_item")],
)
def change_item_C2D2(item):
    if "C2D2-item" in item:
        return accordion_C2D2_content
