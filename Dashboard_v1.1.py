import numpy as np
import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc
from datetime import datetime
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY], meta_tags=[{'name': 'viewport',
                                                                                               'content': 'width=device-width, initial-scale=1.0'}],suppress_callback_exceptions=True)

sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"], className="ms-2"),
            ],
            href=page["path"],
            active="exact",
        )
        for page in dash.page_registry.values()
    ],
    vertical=True,
    pills=True,
    className="bg-light",
)

app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("APM Passenger Traffic Flow Monitoring Dashboard",
                className='text-center text-primary mb-4'), width=12)
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


app.run_server(debug=True)
