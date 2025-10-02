from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Projection Settings")),
                    dbc.CardBody([
                        html.Label("Select Forecast Horizon (Months):"),
                        dcc.Slider(
                            id="projection-horizon-slider",
                            min=3,
                            max=24,
                            step=3,
                            value=12,
                            marks={i: str(i) for i in range(3, 25, 3)}
                        ),
                    ])
                ])
            ], md=12),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("AUM Forecast")),
                    dbc.CardBody([
                        dcc.Graph(id="projection-aum-forecast")
                    ])
                ])
            ], md=12),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Disbursement Forecast")),
                    dbc.CardBody([
                        dcc.Graph(id="projection-disbursement-forecast")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("NPA % Forecast")),
                    dbc.CardBody([
                        dcc.Graph(id="projection-npa-forecast")
                    ])
                ])
            ], md=6),
        ]),
    ], fluid=True, className="mt-4")
