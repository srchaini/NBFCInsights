from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Customer Distribution by Product")),
                    dbc.CardBody([
                        dcc.Graph(id="segmentation-product-pie")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Customer Distribution by Branch")),
                    dbc.CardBody([
                        dcc.Graph(id="segmentation-branch-bar")
                    ])
                ])
            ], md=6),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Risk Band Distribution")),
                    dbc.CardBody([
                        dcc.Graph(id="segmentation-risk-bar")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Product vs Outstanding Amount")),
                    dbc.CardBody([
                        dcc.Graph(id="segmentation-product-amount")
                    ])
                ])
            ], md=6),
        ]),
    ], fluid=True, className="mt-4")
