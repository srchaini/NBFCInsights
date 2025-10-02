from dash import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from my_dash_app.utils.data_loader import generate_time_series_data

def register_callbacks(app):
    @app.callback(
        [Output('projection-aum-forecast', 'figure'),
         Output('projection-disbursement-forecast', 'figure'),
         Output('projection-npa-forecast', 'figure')],
        [Input('projection-horizon-slider', 'value'),
         Input('tabs', 'value')]
    )
    def update_projections(horizon, tab):
        if tab != 'projections':
            return [go.Figure()] * 3
        
        ts_data = generate_time_series_data()
        historical_data = ts_data[ts_data['date'] <= '2025-10-31'].copy()
        
        X = np.arange(len(historical_data)).reshape(-1, 1)
        
        aum_model = LinearRegression()
        aum_model.fit(X, historical_data['aum'])
        
        disb_model = LinearRegression()
        disb_model.fit(X, historical_data['disbursements'])
        
        npa_model = LinearRegression()
        npa_model.fit(X, historical_data['npa_pct'])
        
        future_X = np.arange(len(historical_data), len(historical_data) + horizon).reshape(-1, 1)
        future_dates = pd.date_range(
            start=historical_data['date'].iloc[-1] + pd.DateOffset(months=1),
            periods=horizon,
            freq='M'
        )
        
        aum_forecast = aum_model.predict(future_X)
        disb_forecast = disb_model.predict(future_X)
        npa_forecast = npa_model.predict(future_X)
        
        aum_fig = go.Figure()
        aum_fig.add_trace(go.Scatter(
            x=historical_data['date'],
            y=historical_data['aum'],
            mode='lines',
            name='Historical',
            line=dict(color='#1f77b4', width=2)
        ))
        aum_fig.add_trace(go.Scatter(
            x=future_dates,
            y=aum_forecast,
            mode='lines',
            name='Forecast',
            line=dict(color='#ff7f0e', width=2, dash='dash')
        ))
        aum_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Date',
            yaxis_title='AUM (₹)'
        )
        
        disb_fig = go.Figure()
        disb_fig.add_trace(go.Scatter(
            x=historical_data['date'],
            y=historical_data['disbursements'],
            mode='lines',
            name='Historical',
            line=dict(color='#2ca02c', width=2)
        ))
        disb_fig.add_trace(go.Scatter(
            x=future_dates,
            y=disb_forecast,
            mode='lines',
            name='Forecast',
            line=dict(color='#d62728', width=2, dash='dash')
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
            x=historical_data['date'],
            y=historical_data['npa_pct'],
            mode='lines',
            name='Historical',
            line=dict(color='#9467bd', width=2)
        ))
        npa_fig.add_trace(go.Scatter(
            x=future_dates,
            y=npa_forecast,
            mode='lines',
            name='Forecast',
            line=dict(color='#8c564b', width=2, dash='dash')
        ))
        npa_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title='Date',
            yaxis_title='NPA %'
        )
        
        return aum_fig, disb_fig, npa_fig
