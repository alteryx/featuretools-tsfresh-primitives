import pandas as pd
from featuretools.primitives import AggregationPrimitive, TransformPrimitive
from featuretools.primitives.rolling_primitive_utils import (
    apply_roll_with_offset_gap,
    roll_series_with_gap,
)
from tsfresh.feature_extraction.feature_calculators import fft_aggregated
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Datetime, Double


class FftAggregated(AggregationPrimitive):
    """Returns the spectral centroid (mean), variance, skew, or kurtosis of
    the absolute fourier transform spectrum.

    Args:
        aggtype (str) : Controls which aggregation is returned. Possible values
            are: ["centroid", "variance", "skew", "kurtosis"]

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_aggregated
    """

    name = "fft_aggregated"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, aggtype="centroid"):
        self.aggtype = aggtype

    def get_function(self):
        def function(x):
            param = [{"aggtype": self.aggtype}]
            return list(fft_aggregated(x, param=param))[0][1]

        return function


class ShortTermFftAggregated(TransformPrimitive):
    """Calculates the spectral centroid (mean), variance, skew, or kurtosis of
    the absolute fourier transform spectrum of entries over a given window.

    Description:
        Given a list of numbers and a corresponding list of
        datetimes, return the spectral centroid (mean), variance, skew, or kurtosis of
        the absolute fourier transform spectrum of
        the numeric values, starting at the row `gap` rows away from the current row and
        looking backward over the specified time window
        (by `window_length` and `gap`).

    Args:
        aggtype (str) : Controls which aggregation is returned. Possible values
            are: ["centroid", "variance", "skew", "kurtosis"].
        window_length (int, string, optional): Specifies the amount of data included in each window.
            If an integer is provided, will correspond to a number of rows. For data with a uniform sampling frequency,
            for example of one day, the window_length will correspond to a period of time, in this case,
            7 days for a window_length of 7.
            If a string is provided, it must be one of pandas' offset alias strings ('1D', '1H', etc),
            and it will indicate a length of time that each window should span.
            The list of available offset aliases, can be found at
            https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases.
            Defaults to 3.
        gap (int, string, optional): Specifies a gap backwards from each instance before the
            window of usable data begins. If an integer is provided, will correspond to a number of rows.
            If a string is provided, it must be one of pandas' offset alias strings ('1D', '1H', etc),
            and it will indicate a length of time between a target instance and the beginning of its window.
            Defaults to 0, which will include the target instance in the window.
        min_periods (int, optional): Minimum number of observations required for performing calculations
            over the window. Can only be as large as window_length when window_length is an integer.
            When window_length is an offset alias string, this limitation does not exist, but care should be taken
            to not choose a min_periods that will always be larger than the number of observations in a window.
            Defaults to 1.

    Note:
        Only offset aliases with fixed frequencies can be used when defining gap and window_length.
        This means that aliases such as `M` or `W` cannot be used, as they can indicate different
        numbers of days. ('M', because different months are different numbers of days;
        'W' because week will indicate a certain day of the week, like W-Wed, so that will
        indicate a different number of days depending on the anchoring date.)

    Note:
        When using an offset alias to define `gap`, an offset alias must also be used to define `window_length`.
        This limitation does not exist when using an offset alias to define `window_length`. In fact,
        if the data has a uniform sampling frequency, it is preferable to use a numeric `gap` as it is more
        efficient.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_aggregated

    Examples:
        >>> import pandas as pd
        >>> datetimes = pd.date_range(start="2019-01-01", freq="1D", periods=10)
        >>> stffta = ShortTermFftAggregated(aggtype="centroid")
        >>> output = stffta(datetimes, [1, 2, 4, 8, 4, 2, 1, 2, 4, 8]).tolist()
        >>> [round(x, 5) for x in output]
        [0.0, 0.25, 0.27429, 0.27429, 0.2, 0.27429, 0.27429, 0.16667, 0.27429, 0.27429]

        We can also control the gap before the rolling calculation.

        >>> stffta = ShortTermFftAggregated(aggtype="centroid", gap=1)
        >>> output = stffta(datetimes, [1, 2, 4, 8, 4, 2, 1, 2, 4, 8]).tolist()
        >>> [round(x, 5) for x in output]
        [nan, nan, nan, 0.27429, 0.27429, 0.2, 0.27429, 0.27429, 0.16667, 0.27429]

        We can also control the aggregation type.

        >>> stffta = ShortTermFftAggregated(aggtype="variance")
        >>> output = stffta(datetimes, [1, 2, 4, 8, 4, 2, 1, 2, 4, 8]).tolist()
        >>> [round(x, 5) for x in output]
        [0.0, 0.1875, 0.19906, 0.19906, 0.16, 0.19906, 0.19906, 0.13889, 0.19906, 0.19906]
    """

    name = "short_term_fft_aggregated"
    input_types = [
        ColumnSchema(logical_type=Datetime, semantic_tags={"time_index"}),
        ColumnSchema(semantic_tags={"numeric"}),
    ]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})

    def __init__(self, aggtype="centroid", window_length=3, gap=0, min_periods=0):
        self.aggtype = aggtype
        self.window_length = window_length
        self.gap = gap
        self.min_periods = min_periods

    def get_function(self):
        def short_term_fft_aggregated(datetime, numeric):
            x = pd.Series(numeric.values, index=datetime.values)
            rolled_series = roll_series_with_gap(
                x, self.window_length, gap=self.gap, min_periods=self.min_periods
            )
            if isinstance(self.gap, str):
                additional_args = (
                    self.gap,
                    self.appliable_fft_aggregated,
                    self.min_periods,
                )
                return rolled_series.apply(
                    apply_roll_with_offset_gap,
                    args=additional_args,
                ).values
            return rolled_series.apply(self.appliable_fft_aggregated).values

        return short_term_fft_aggregated

    def appliable_fft_aggregated(self, series):
        param = [{"aggtype": self.aggtype}]
        return list(fft_aggregated(series.values, param=param))[0][1]
