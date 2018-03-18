
import numpy as np
import pandas as pd

def nps(series):
    """
    Net Promoter Score(R)
    http://www.netpromotersystem.com/resources/trademarks-and-licensing.aspx

    Subtract percentage of promoters from percentage of detractors.
    - Detractors - 6 and below
    - Passives - 7,8
    - Promoters - 9,10
    """
    promoters = series >= 9
    detractors = series <= 6
    total = float(series.count())

    return int(100 * (promoters.sum() / total - detractors.sum() / total))

df = pd.read_csv('nps-developer-survey.csv')

# Sometimes only looking at a segment
filtered = df
# filtered = df.loc[df['Business'] == 'foo']

# Just dump to stdout descriptive statistics along with nps for each sample
for col in df.columns[1:]:
    series = filtered[col].dropna()
    print(col, series.count(), series.mean(), series.std(), nps(series))
