import pandas as pd
from featuretools.primitives import AggregationPrimitive, TransformPrimitive
from featuretools.primitives.rolling_primitive_utils import (
    apply_roll_with_offset_gap,
    roll_series_with_gap,
)
from tsfresh.feature_extraction.feature_calculators import fft_coefficient
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Datetime, Double


class FftCoefficient(AggregationPrimitive):
    """Calculates the fourier coefficients of the one-dimensional discrete
    Fourier Transform for real input by fast fourier transformation algorithm

    .. math::
        A_k =  \\sum_{m=0}^{n-1} a_m \\exp \\left \\{ -2 \\pi i \\frac{m k}{n} \\right \\}, \\qquad k = 0,
        \\ldots , n-1.

    The resulting coefficients will be complex, this feature calculator can
    return the real part (attr=="real"), the imaginary part (attr=="imag"), the
    absolute value (attr="abs") and the angle in degrees (attr=="angle").

    Args:
        coeff (int) : The coefficient to return. Must be greater than or equal to zero.
        attr (str) : Controls which attribute is returned.
            Possible values are: ["real", "imag", "abs", "angle"]

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_coefficient
    """

    name = "fft_coefficient"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, coeff=1, attr="real"):
        self.coeff = coeff
        self.attr = attr

    def get_function(self):
        def function(x):
            param = [{"coeff": self.coeff, "attr": self.attr}]
            return list(fft_coefficient(x, param=param))[0][1]

        return function


class ShortTermFftCoefficient(TransformPrimitive):
    """Calculates the fourier coefficients of the one-dimensional discrete
    Fourier Transform for real input by fast fourier transformation algorithm over a given window.

    .. math::
        A_k =  \\sum_{m=0}^{n-1} a_m \\exp \\left \\{ -2 \\pi i \\frac{m k}{n} \\right \\}, \\qquad k = 0,
        \\ldots , n-1.

    The resulting coefficients will be complex, this feature calculator can
    return the real part (attr=="real"), the imaginary part (attr=="imag"), the
    absolute value (attr="abs") and the angle in degrees (attr=="angle").

    Description:
        Given a list of numbers and a corresponding list of
        datetimes, return the fourier coefficients of the one-dimensional discrete
        Fourier Transform of the numeric values, starting at the row `gap` rows away from the current row and
        looking backward over the specified time window
        (by `window_length` and `gap`).

    Args:
        coeff (int) : The coefficient to return. Must be greater than or equal to zero.
        attr (str) : Controls which attribute is returned.
            Possible values are: ["real", "imag", "abs", "angle"]
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
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_coefficient

    Examples:
        >>> import pandas as pd
        >>> datetimes = pd.date_range(start="2019-01-01", freq="1D", periods=10)
        >>> stfftc = ShortTermFftCoefficient(1, "real")
        >>> stfftc(datetimes, [1, 2, 4, 8, 16, 24, 48, 96, 192, 384]).tolist()
        [nan, -1.0, -2.0, -4.0, -8.0, -12.0, -20.0, -48.0, -96.0, -192.0]

        We can also control the gap before the rolling calculation.

        >>> stfftc = ShortTermFftCoefficient(1, "real", gap=1)
        >>> stfftc(datetimes, [1, 2, 4, 8, 16, 24, 48, 96, 192, 384]).tolist()
        [nan, nan, nan, -2.0, -4.0, -8.0, -12.0, -20.0, -48.0, -96.0]

        We can also control the attribute type.

        >>> stfftc = ShortTermFftCoefficient(1, "imag")
        >>> stfftc(datetimes, [1, 2, 4, 8, 16, 24, 48, 96, 192, 384]).tolist()
        [nan, 0.0, 1.7320508075688772, 3.4641016151377544, 6.928203230275509, 6.928203230275509, 20.784609690826528, 41.569219381653056, 83.13843876330611, 166.27687752661222]

    """

    name = "short_term_fft_coefficient"
    input_types = [
        ColumnSchema(logical_type=Datetime, semantic_tags={"time_index"}),
        ColumnSchema(semantic_tags={"numeric"}),
    ]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})

    def __init__(self, coeff=1, attr="real", window_length=3, gap=0, min_periods=0):
        self.coeff = coeff
        self.attr = attr
        self.window_length = window_length
        self.gap = gap
        self.min_periods = min_periods

    def get_function(self):
        def short_term_fft_coefficient(datetime, numeric):
            x = pd.Series(numeric.values, index=datetime.values)
            rolled_series = roll_series_with_gap(
                x, self.window_length, gap=self.gap, min_periods=self.min_periods
            )
            if isinstance(self.gap, str):
                additional_args = (
                    self.gap,
                    self.appliable_fft_coefficient,
                    self.min_periods,
                )
                return rolled_series.apply(
                    apply_roll_with_offset_gap,
                    args=additional_args,
                ).values
            return rolled_series.apply(self.appliable_fft_coefficient).values

        return short_term_fft_coefficient

    def appliable_fft_coefficient(self, series):
        param = [{"coeff": self.coeff, "attr": self.attr}]
        return list(fft_coefficient(series.values, param=param))[0][1]
