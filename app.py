import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from my_dash_app.layout import portfolio_layout, segmentation_layout, collections_layout, branch_layout, projections_layout
from my_dash_app.callbacks import portfolio_callbacks, segmentation_callbacks, collections_callbacks, branch_callbacks, projections_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # <- This is required for Render
app.title = "NBFC Dashboard"

app.layout = dbc.Container([
    html.H1("NBFC Analytics Dashboard", className="text-center my-4"),
    
    dcc.Tabs(id='tabs', value='portfolio', children=[
        dcc.Tab(label='Portfolio Overview', value='portfolio'),
        dcc.Tab(label='Customer Segmentation', value='segmentation'),
        dcc.Tab(label='Collections & Risk', value='collections'),
        dcc.Tab(label='Branch Performance', value='branch'),
        dcc.Tab(label='Future Projections', value='projections'),
    ]),
    
    html.Div(id='tab-content', children=[
        html.Div(id='portfolio-content', children=portfolio_layout.create_layout()),
        html.Div(id='segmentation-content', children=segmentation_layout.create_layout(), style={'display': 'none'}),
        html.Div(id='collections-content', children=collections_layout.create_layout(), style={'display': 'none'}),
        html.Div(id='branch-content', children=branch_layout.create_layout(), style={'display': 'none'}),
        html.Div(id='projections-content', children=projections_layout.create_layout(), style={'display': 'none'}),
    ])
], fluid=True)

@app.callback(
    [dash.Output('portfolio-content', 'style'),
     dash.Output('segmentation-content', 'style'),
     dash.Output('collections-content', 'style'),
     dash.Output('branch-content', 'style'),
     dash.Output('projections-content', 'style')],
    [dash.Input('tabs', 'value')]
)
def render_content(tab):
    styles = [{'display': 'none'}] * 5
    tab_index = {'portfolio': 0, 'segmentation': 1, 'collections': 2, 'branch': 3, 'projections': 4}
    if tab in tab_index:
        styles[tab_index[tab]] = {'display': 'block'}
    return styles

portfolio_callbacks.register_callbacks(app)
segmentation_callbacks.register_callbacks(app)
collections_callbacks.register_callbacks(app)
branch_callbacks.register_callbacks(app)
projections_callbacks.register_callbacks(app)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
