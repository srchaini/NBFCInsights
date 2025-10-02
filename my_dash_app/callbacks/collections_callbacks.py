from dash import Input, Output
import plotly.graph_objs as go
from my_dash_app.utils.data_loader import generate_nbfc_data, get_monthly_collection_data
from my_dash_app.utils.kpi_functions import calculate_par, calculate_collection_efficiency, get_dpd_buckets, format_currency

def register_callbacks(app):
    @app.callback(
        [Output('collections-par', 'children'),
         Output('collections-efficiency', 'children'),
         Output('collections-npa-amount', 'children'),
         Output('collections-dpd-buckets', 'figure'),
         Output('collections-par-curve', 'figure'),
         Output('collections-monthly-efficiency', 'figure')],
        [Input('tabs', 'value')]
    )
    def update_collections(tab):
        if tab != 'collections':
            return [''] * 3 + [go.Figure()] * 3
        
        df = generate_nbfc_data()
        monthly_data = get_monthly_collection_data()
        
        par = calculate_par(df)
        coll_eff = calculate_collection_efficiency(df)
        npa_amount = df[df['npa_flag'] == 1]['outstanding_amount'].sum()
        
        dpd_buckets = get_dpd_buckets(df)
        dpd_fig = go.Figure(data=[go.Bar(
            x=dpd_buckets['Bucket'],
            y=dpd_buckets['Count'],
            marker_color=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728', '#8b0000']
        )])
        dpd_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='DPD Bucket',
            yaxis_title='Count'
        )
        
        par_curve_data = df.groupby('dpd')['outstanding_amount'].sum().reset_index()
        par_curve_data = par_curve_data.sort_values('dpd')
        par_curve_data['cumulative_par'] = par_curve_data['outstanding_amount'].cumsum()
        total_outstanding = df['outstanding_amount'].sum()
        par_curve_data['par_pct'] = (par_curve_data['cumulative_par'] / total_outstanding * 100)
        
        par_fig = go.Figure(data=[go.Scatter(
            x=par_curve_data['dpd'],
            y=par_curve_data['par_pct'],
            mode='lines+markers',
            line=dict(color='#d62728', width=2)
        )])
        par_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='DPD',
            yaxis_title='PAR %'
        )
        
        monthly_fig = go.Figure(data=[go.Bar(
            x=monthly_data['month'],
            y=monthly_data['collection_efficiency'],
            marker_color='#2ca02c'
        )])
        monthly_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Month',
            yaxis_title='Collection Efficiency %'
        )
        
        return (
            f"{par:.2f}%",
            f"{coll_eff:.2f}%",
            format_currency(npa_amount),
            dpd_fig,
            par_fig,
            monthly_fig
        )
