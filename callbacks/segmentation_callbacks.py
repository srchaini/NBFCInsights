from dash import Input, Output
import plotly.graph_objs as go
from my_dash_app.utils.data_loader import generate_nbfc_data

def register_callbacks(app):
    @app.callback(
        [Output('segmentation-product-pie', 'figure'),
         Output('segmentation-branch-bar', 'figure'),
         Output('segmentation-risk-bar', 'figure'),
         Output('segmentation-product-amount', 'figure')],
        [Input('tabs', 'value')]
    )
    def update_segmentation(tab):
        if tab != 'segmentation':
            return [go.Figure()] * 4
        
        df = generate_nbfc_data()
        
        product_dist = df['product'].value_counts()
        product_pie = go.Figure(data=[go.Pie(
            labels=product_dist.index,
            values=product_dist.values,
            hole=0.4
        )])
        product_pie.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            title='Product Distribution'
        )
        
        branch_dist = df['branch'].value_counts().sort_values(ascending=True)
        branch_bar = go.Figure(data=[go.Bar(
            x=branch_dist.values,
            y=branch_dist.index,
            orientation='h',
            marker_color='#ff7f0e'
        )])
        branch_bar.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            title='Branch Distribution',
            xaxis_title='Number of Customers',
            yaxis_title='Branch'
        )
        
        risk_dist = df['risk_band'].value_counts()
        risk_bar = go.Figure(data=[go.Bar(
            x=risk_dist.index,
            y=risk_dist.values,
            marker_color=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']
        )])
        risk_bar.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            title='Risk Band Distribution',
            xaxis_title='Risk Band',
            yaxis_title='Count'
        )
        
        product_amount = df.groupby('product')['outstanding_amount'].sum().sort_values(ascending=True)
        product_amount_fig = go.Figure(data=[go.Bar(
            x=product_amount.values,
            y=product_amount.index,
            orientation='h',
            marker_color='#9467bd'
        )])
        product_amount_fig.update_layout(
            template='plotly_white',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            title='Outstanding by Product',
            xaxis_title='Outstanding Amount (₹)',
            yaxis_title='Product'
        )
        
        return product_pie, branch_bar, risk_bar, product_amount_fig
