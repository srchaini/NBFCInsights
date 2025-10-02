from dash import Input, Output
import plotly.graph_objs as go
from utils.data_loader import generate_time_series_data
from utils.kpi_functions import format_currency

def register_callbacks(app):
    @app.callback(
        [Output('portfolio-aum', 'children'),
         Output('portfolio-aum-change', 'children'),
         Output('portfolio-disbursements', 'children'),
         Output('portfolio-disbursements-change', 'children'),
         Output('portfolio-npa', 'children'),
         Output('portfolio-npa-change', 'children'),
         Output('portfolio-aum-trend', 'figure'),
         Output('portfolio-disbursement-trend', 'figure'),
         Output('portfolio-npa-trend', 'figure')],
        [Input('tabs', 'value')]
    )
    def update_portfolio(tab):
        if tab != 'portfolio':
            return [''] * 6 + [go.Figure()] * 3
        
        ts_data = generate_time_series_data()
        
        current_aum = ts_data['aum'].iloc[-1]
        prev_aum = ts_data['aum'].iloc[-2]
        aum_change = ((current_aum - prev_aum) / prev_aum * 100)
        
        current_disb = ts_data['disbursements'].iloc[-1]
        prev_disb = ts_data['disbursements'].iloc[-2]
        disb_change = ((current_disb - prev_disb) / prev_disb * 100)
        
        current_npa = ts_data['npa_pct'].iloc[-1]
        prev_npa = ts_data['npa_pct'].iloc[-2]
        npa_change = current_npa - prev_npa
        
        aum_fig = go.Figure()
        aum_fig.add_trace(go.Scatter(
            x=ts_data['date'],
            y=ts_data['aum'],
            mode='lines+markers',
            name='AUM',
            line=dict(color='#1f77b4', width=2)
        ))
        aum_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Date',
            yaxis_title='AUM (₹)'
        )
        
        disb_fig = go.Figure()
        disb_fig.add_trace(go.Bar(
            x=ts_data['date'],
            y=ts_data['disbursements'],
            name='Disbursements',
            marker_color='#2ca02c'
        ))
        disb_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Date',
            yaxis_title='Disbursements (₹)'
        )
        
        npa_fig = go.Figure()
        npa_fig.add_trace(go.Scatter(
            x=ts_data['date'],
            y=ts_data['npa_pct'],
            mode='lines+markers',
            name='NPA %',
            line=dict(color='#d62728', width=2)
        ))
        npa_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Date',
            yaxis_title='NPA %'
        )
        
        return (
            format_currency(current_aum),
            f"↑ {aum_change:.2f}% from last month",
            format_currency(current_disb),
            f"↑ {disb_change:.2f}% from last month",
            f"{current_npa:.2f}%",
            f"↑ {npa_change:.2f}% from last month",
            aum_fig,
            disb_fig,
            npa_fig
        )
