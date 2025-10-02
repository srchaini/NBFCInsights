from dash import Input, Output, html
import plotly.graph_objs as go
import pandas as pd
from utils.data_loader import generate_nbfc_data
from utils.kpi_functions import get_branch_performance

def register_callbacks(app):
    @app.callback(
        Output('branch-filter-dropdown', 'options'),
        [Input('tabs', 'value')]
    )
    def set_branch_options(tab):
        if tab != 'branch':
            return []
        df = generate_nbfc_data()
        branches = sorted(df['branch'].unique())
        return [{'label': branch, 'value': branch} for branch in branches]
    
    @app.callback(
        [Output('branch-performance-table', 'children'),
         Output('branch-outstanding-bar', 'figure'),
         Output('branch-npa-bar', 'figure')],
        [Input('branch-filter-dropdown', 'value'),
         Input('tabs', 'value')]
    )
    def update_branch_performance(selected_branches, tab):
        if tab != 'branch':
            return html.Div(), go.Figure(), go.Figure()
        
        df = generate_nbfc_data()
        
        if selected_branches:
            df = df[df['branch'].isin(selected_branches)]
        
        branch_stats = get_branch_performance(df)
        
        table = html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in branch_stats.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(branch_stats.iloc[i][col]) for col in branch_stats.columns
                ]) for i in range(len(branch_stats))
            ])
        ], className='table table-striped table-hover')
        
        outstanding_fig = go.Figure(data=[go.Bar(
            x=branch_stats['Branch'],
            y=branch_stats['Outstanding'],
            marker_color='#1f77b4'
        )])
        outstanding_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Branch',
            yaxis_title='Outstanding Amount (₹)'
        )
        
        npa_fig = go.Figure(data=[go.Bar(
            x=branch_stats['Branch'],
            y=branch_stats['NPA %'],
            marker_color='#d62728'
        )])
        npa_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Branch',
            yaxis_title='NPA %'
        )
        
        return table, outstanding_fig, npa_fig
