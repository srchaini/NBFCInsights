from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Total AUM", className="text-muted mb-2"),
                        html.H3(id="portfolio-aum", className="mb-0"),
                        html.Small(id="portfolio-aum-change", className="text-success")
                    ])
                ], className="kpi-card")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Total Disbursements", className="text-muted mb-2"),
                        html.H3(id="portfolio-disbursements", className="mb-0"),
                        html.Small(id="portfolio-disbursements-change", className="text-success")
                    ])
                ], className="kpi-card")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("NPA %", className="text-muted mb-2"),
                        html.H3(id="portfolio-npa", className="mb-0"),
                        html.Small(id="portfolio-npa-change", className="text-danger")
                    ])
                ], className="kpi-card")
            ], md=4),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("AUM Trend")),
                    dbc.CardBody([
                        dcc.Graph(id="portfolio-aum-trend")
                    ])
                ])
            ], md=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("Disbursement Volume")),
                    dbc.CardBody([
                        dcc.Graph(id="portfolio-disbursement-trend")
                    ])
                ])
            ], md=6),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H5("NPA % Trend")),
                    dbc.CardBody([
                        dcc.Graph(id="portfolio-npa-trend")
                    ])
                ])
            ], md=12),
        ]),
    ], fluid=True, className="mt-4")
