import pandas as pd
import numpy as np

def calculate_aum(df):
    return df['outstanding_amount'].sum()

def calculate_total_disbursements(df):
    return df['disbursement_amount'].sum()

def calculate_npa_percentage(df):
    total = len(df)
    npa_count = df['npa_flag'].sum()
    return (npa_count / total * 100) if total > 0 else 0

def calculate_par(df):
    total_outstanding = df['outstanding_amount'].sum()
    if total_outstanding == 0:
        return 0
    par_outstanding = df[df['dpd'] > 0]['outstanding_amount'].sum()
    return (par_outstanding / total_outstanding * 100)

def get_dpd_buckets(df):
    buckets = {
        '0 DPD': len(df[df['dpd'] == 0]),
        '1-30 DPD': len(df[(df['dpd'] > 0) & (df['dpd'] <= 30)]),
        '31-60 DPD': len(df[(df['dpd'] > 30) & (df['dpd'] <= 60)]),
        '61-90 DPD': len(df[(df['dpd'] > 60) & (df['dpd'] <= 90)]),
        '90+ DPD': len(df[df['dpd'] > 90])
    }
    return pd.DataFrame(list(buckets.items()), columns=['Bucket', 'Count'])

def get_product_distribution(df):
    return df['product'].value_counts().reset_index()

def get_branch_performance(df):
    branch_stats = df.groupby('branch').agg({
        'outstanding_amount': 'sum',
        'disbursement_amount': 'sum',
        'npa_flag': 'sum',
        'borrower_id': 'count'
    }).reset_index()
    
    branch_stats.columns = ['Branch', 'Outstanding', 'Disbursements', 'NPA Count', 'Total Loans']
    branch_stats['NPA %'] = (branch_stats['NPA Count'] / branch_stats['Total Loans'] * 100).round(2)
    
    return branch_stats

def calculate_collection_efficiency(df):
    total_emi = df['emi_amount'].sum()
    collected = df[df['dpd'] == 0]['emi_amount'].sum()
    return (collected / total_emi * 100) if total_emi > 0 else 0

def format_currency(value):
    if value >= 10000000:
        return f'₹{value/10000000:.2f} Cr'
    elif value >= 100000:
        return f'₹{value/100000:.2f} L'
    else:
        return f'₹{value:,.0f}'
