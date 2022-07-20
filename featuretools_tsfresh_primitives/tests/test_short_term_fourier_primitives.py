from numpy import nan
from pandas import Series, date_range, testing
from pytest import fixture, mark

from featuretools_tsfresh_primitives import (
    ShortTermFftAggregated,
    ShortTermFftCoefficient,
)


@fixture
def rolling_series_pd():
    return Series(
        [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4],
        index=date_range(start="2020-01-01", end="2020-01-20"),
    )


@mark.parametrize(
    "window_length,gap,expected_vals",
    [
        (
            3,
            1,
            [
                nan,
                nan,
                nan,
                0.22400924,
                0.16139048,
                0.12613198,
                0.07142857,
                0.12613198,
                0.16139048,
                0.22400924,
                0.16666667,
                0.22400924,
                0.16139048,
                0.12613198,
                0.07142857,
                0.12613198,
                0.16139048,
                0.22400924,
                0.16666667,
                0.22400924,
            ],
        ),
        (
            4,
            2,
            [
                nan,
                nan,
                nan,
                nan,
                nan,
                0.46049571,
                0.36266583,
                0.11111111,
                0.11111111,
                0.36266583,
                0.46049571,
                0.2,
                0.2,
                0.46049571,
                0.36266583,
                0.11111111,
                0.11111111,
                0.36266583,
                0.46049571,
                0.2,
            ],
        ),
        (
            "5d",
            "7d",
            [
                nan,
                nan,
                nan,
                nan,
                nan,
                nan,
                nan,
                0,
                0.25,
                0.22400924,
                0.46049571,
                0.43463141,
                0.24006091,
                0.15372573,
                0.24006091,
                0.43463141,
                0.32772268,
                0.241569,
                0.32772268,
                0.43463141,
            ],
        ),
    ],
)
def test_short_term_fourier_agg(window_length, gap, expected_vals, rolling_series_pd):
    primitive_instance = ShortTermFftAggregated(
        aggtype="centroid", window_length=window_length, gap=gap
    )

    actual_vals = primitive_instance(rolling_series_pd.index, rolling_series_pd.values)

    testing.assert_series_equal(Series(expected_vals), Series(actual_vals))


@mark.parametrize(
    "window_length,gap,expected_vals",
    [
        (
            3,
            1,
            [
                nan,
                nan,
                nan,
                -1.5,
                -1.5,
                -1.5,
                -0.5,
                1.5,
                1.5,
                1.5,
                0.5,
                -1.5,
                -1.5,
                -1.5,
                -0.5,
                1.5,
                1.5,
                1.5,
                0.5,
                -1.5,
            ],
        ),
        (
            4,
            2,
            [
                nan,
                nan,
                nan,
                nan,
                nan,
                -2,
                -2,
                -2,
                0,
                2,
                2,
                2,
                0,
                -2,
                -2,
                -2,
                0,
                2,
                2,
                2,
            ],
        ),
        (
            "5d",
            "7d",
            [
                nan,
                nan,
                nan,
                nan,
                nan,
                nan,
                nan,
                nan,
                -1,
                -1.5,
                -2,
                -2.5,
                -3.11803399,
                -2.11803399,
                0.5,
                2.5,
                3.11803399,
                2.11803399,
                -0.5,
                -2.5,
            ],
        ),
    ],
)
def test_short_term_fourier_coeff(window_length, gap, expected_vals, rolling_series_pd):
    primitive_instance = ShortTermFftCoefficient(
        coeff=1, attr="real", window_length=window_length, gap=gap
    )

    actual_vals = primitive_instance(rolling_series_pd.index, rolling_series_pd.values)

    testing.assert_series_equal(Series(expected_vals), Series(actual_vals))
