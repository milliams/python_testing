from hypothesis import given
from hypothesis.extra.pandas import columns, data_frames, range_indexes
import hypothesis.strategies as st
import pandas as pd

from analyse_weather import get_data, hottest_summer


@given(
    data_frames(
        columns=columns(
            ['JUN', 'JUL', 'AUG'],
            elements=st.floats(allow_nan=True)
        ),
        index=range_indexes(min_size=1)
    )
)
def test_hottest_summer_auto(df):
    assert not pd.isnull(hottest_summer(df))


# Below is annother example of using fixtures but for this function:
import pytest
from pandas import DataFrame


@pytest.fixture
def full_dataset():
    return get_data()


@pytest.fixture
def small_dataset():
    return DataFrame(data={
        'JAN' : [0.2, 0.7, 4.6, 2.3],
        'FEB' : [4.3, 3.6, 6.4, 2.5],
        'MAR' : [7.4, 6.4, 8.0, 5.6],
        'APR' : [7.6, 5.6, 8.7, 9.1],
        'MAY' : [10.3, 6.7, 9.8, 11.0],
        'JUN' : [14.6, 16.0, 12.5, 14.4],
        'JUL' : [14.5, 13.9, 12.6, 13.7],
        'AUG' : [15.8, 13.8, 12.0, 14.1],
        'SEP' : [12.6, 10.6, 10.6, 9.8],
        'OCT' : [9.8, 10.0, 9.7, 8.5],
        'NOV' : [5.8, 3.7, 6.8, 9.4],
        'DEC' : [3.7, 3.6, 2.9, 4.8],
        'YEAR' : [6.5, 7.4, 4.6, 6.8],
        },
        index=[1990, 1991, 1992, 1993],
    )


def test_hottest_summer_full(full_dataset):
    assert hottest_summer(full_dataset) == 2006


def test_hottest_summer_small(small_dataset):
    assert hottest_summer(small_dataset) == 1991
