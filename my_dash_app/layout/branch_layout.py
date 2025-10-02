from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Branch Filters")),
                    dbc.CardBody([
                        html.Label("Select Branch:"),
                        dcc.Dropdown(
                            id="branch-filter-dropdown",
                            multi=True,
                            placeholder="Select branches..."
                        ),
                    ])
                ])
            ], md=12),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Branch Performance Table")),
                    dbc.CardBody([
                        html.Div(id="branch-performance-table")
                    ])
                ])
            ], md=12),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Branch-wise Outstanding Amount")),
                    dbc.CardBody([
                        dcc.Graph(id="branch-outstanding-bar")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Branch-wise NPA %")),
                    dbc.CardBody([
                        dcc.Graph(id="branch-npa-bar")
                    ])
                ])
            ], md=6),
        ]),
    ], fluid=True, className="mt-4")
