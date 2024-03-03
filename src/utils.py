import pandas as pd


def arrangepercentage(p) -> float:
    if type(p) == str:
        return float(p.replace('%', ''))
    else:
        return p


def arrangestringfloat(s) -> float:
    if type(s) == str:
        return float(s.replace(',', ''))
    else:
        return s


SIZE_METRICS = ['LOC']
INTERFACE_COMPLEXITY = ['SIZE2', 'NOM']
STRUCTURAL_COMPLEXITY = ['CC', 'WMC', 'RFC']
HERITAGE = ['DIT', 'NOC']
COUPLAGE = ['Ca', 'CBO']
COHESION = ['LCOM', 'TCC']
DOCUMENTATION = ['LOD']


def computemetrics(df: pd.DataFrame) -> pd.DataFrame:
    description = df.describe().loc[['mean', 'std', 'max', 'min']].T
    totals = df.sum()
    return pd.merge(description, pd.DataFrame(totals), left_index=True, right_index=True).rename(columns={0: 'Total'})


def ispackage(value):
    return value.count('.') == 3
