import numpy as np
import pandas as pd
import pytest

from pandas import DataFrame


def get_data():
    """
    Read the full data set from file and return it as a Pandas DataFrame
    """
    return pd.read_csv(
        'cetml1659on.dat',
        skiprows=6,
        sep='\s+',
        na_values=['-99.9', '-99.99'],
    )


def hottest_summer(df) -> int:
    """
    Find the year with the highest average monthly temperature
    """
    df['summer_max'] = df[['JUN', 'JUL', 'AUG']].max(axis=1)
    hottest_year = df['summer_max'].idxmax()
    return hottest_year
