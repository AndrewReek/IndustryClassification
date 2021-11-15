import pandas as pd

def sic_simple_classification(df, sic_col):
    df['Industry_Class'] = ''
    df.loc[(df[sic_col] >= 100) & (df[sic_col] <= 999), 'Industry'] = '[0] Agriculture, Forestry, Fishing'
    df.loc[(df[sic_col] >= 1000) & (df[sic_col] <= 1799), 'Industry'] = '[1] Mining and Construction'
    df.loc[(df[sic_col] >= 2000) & (df[sic_col] <= 2999), 'Industry'] = '[2] Light Manufacturing'
    df.loc[(df[sic_col] >= 3000) & (df[sic_col] <= 3999), 'Industry'] = '[3] Heavy Manufacturing'
    df.loc[(df[sic_col] >= 4000) & (df[sic_col] <= 4999), 'Industry'] = '[4] Transportation and Public Utility'
    df.loc[(df[sic_col] >= 5000) & (df[sic_col] <= 5999), 'Industry'] = '[5] Wholesale and Retail'
    df.loc[(df[sic_col] >= 6000) & (df[sic_col] <= 6999), 'Industry'] = '[6] Finance, Insurance, Real Estate'
    df.loc[(df[sic_col] >= 7000) & (df[sic_col] <= 8999), 'Industry'] = '[7 & 8] Services'
    df.loc[(df[sic_col] >= 9100) & (df[sic_col] <= 9729), 'Industry'] = '[9] Public Administration'
    df.loc[(df[sic_col] >= 9900) & (df[sic_col] <= 9999), 'Industry'] = 'Nonclassifiable'

    return df