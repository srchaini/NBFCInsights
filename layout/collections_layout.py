from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("PAR (Portfolio at Risk)", className="text-muted mb-2"),
                        html.H3(id="collections-par", className="mb-0"),
                    ])
                ], className="kpi-card")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Collection Efficiency", className="text-muted mb-2"),
                        html.H3(id="collections-efficiency", className="mb-0"),
                    ])
                ], className="kpi-card")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Total NPA Amount", className="text-muted mb-2"),
                        html.H3(id="collections-npa-amount", className="mb-0"),
                    ])
                ], className="kpi-card")
            ], md=4),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("DPD Buckets")),
                    dbc.CardBody([
                        dcc.Graph(id="collections-dpd-buckets")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("PAR Curve")),
                    dbc.CardBody([
                        dcc.Graph(id="collections-par-curve")
                    ])
                ])
            ], md=6),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Monthly Collection Efficiency")),
                    dbc.CardBody([
                        dcc.Graph(id="collections-monthly-efficiency")
                    ])
                ])
            ], md=12),
        ]),
    ], fluid=True, className="mt-4")
