import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_nbfc_data(n_records=1000):
    np.random.seed(42)
    
    branches = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
    products = ['Personal Loan', 'Business Loan', 'Vehicle Loan', 'Gold Loan', 'Home Loan']
    risk_bands = ['Low', 'Medium', 'High', 'Very High']
    
    start_date = datetime.now() - timedelta(days=730)
    
    data = {
        'borrower_id': [f'BR{str(i).zfill(6)}' for i in range(1, n_records + 1)],
        'branch': np.random.choice(branches, n_records),
        'product': np.random.choice(products, n_records, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        'disbursement_date': [start_date + timedelta(days=int(x)) for x in np.random.uniform(0, 730, n_records)],
        'disbursement_amount': np.random.uniform(50000, 2000000, n_records).astype(int),
        'outstanding_amount': np.random.uniform(10000, 1500000, n_records).astype(int),
        'dpd': np.random.choice([0, 1, 15, 30, 45, 60, 90, 120, 150, 180], n_records, 
                                p=[0.65, 0.10, 0.08, 0.05, 0.04, 0.03, 0.02, 0.015, 0.01, 0.005]),
        'risk_band': np.random.choice(risk_bands, n_records, p=[0.4, 0.35, 0.2, 0.05]),
        'interest_rate': np.random.uniform(8, 18, n_records).round(2),
        'emi_amount': np.random.uniform(5000, 50000, n_records).astype(int),
        'tenure_months': np.random.choice([12, 24, 36, 48, 60, 72], n_records),
    }
    
    df = pd.DataFrame(data)
    df['npa_flag'] = (df['dpd'] >= 90).astype(int)
    df['collection_efficiency'] = np.where(df['dpd'] == 0, 
                                           np.random.uniform(95, 100, n_records),
                                           np.random.uniform(50, 95, n_records)).round(2)
    
    return df

def generate_time_series_data():
    dates = pd.date_range(start='2023-01-01', end='2025-12-31', freq='ME')
    n_months = len(dates)
    
    base_aum = 5000000000
    trend = np.linspace(0, base_aum * 0.3, n_months)
    seasonal = base_aum * 0.05 * np.sin(np.arange(n_months) * 2 * np.pi / 12)
    noise = np.random.normal(0, base_aum * 0.02, n_months)
    
    aum = base_aum + trend + seasonal + noise
    
    disbursements = aum * np.random.uniform(0.08, 0.15, n_months)
    
    npa_base = np.random.uniform(2, 4, n_months)
    npa_trend = np.linspace(0, 1, n_months)
    npa_pct = npa_base + npa_trend + np.random.normal(0, 0.3, n_months)
    npa_pct = np.clip(npa_pct, 1, 6)
    
    ts_data = pd.DataFrame({
        'date': dates,
        'aum': aum.astype(int),
        'disbursements': disbursements.astype(int),
        'npa_pct': npa_pct.round(2)
    })
    
    return ts_data

def get_monthly_collection_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    collection_efficiency = np.random.uniform(85, 98, 12).round(2)
    
    return pd.DataFrame({
        'month': months,
        'collection_efficiency': collection_efficiency
    })
