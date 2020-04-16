from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import DatetimeTimeIndex, Numeric
from tsfresh.feature_extraction.feature_calculators import \
    linear_trend_timewise


class LinearTrendTimewise(AggregationPrimitive):
    """Calculate a linear least-squares regression for the values of the time series versus the sequence from 0 to length of the time series minus one.
    This feature uses the index of the time series to fit the model, which must be of a datetime dtype. The parameters control which of the characteristics are returned.
    Possible extracted attributes are "pvalue", "rvalue", "intercept", "slope", "stderr", see the documentation of linregress for more information.

    Args:
        attr (str) : Controls which of the characteristics are returned.
            Possible extracted attributes are: pvalue, rvalue, intercept, slope, or stderr.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.linear_trend_timewise
    """
    name = "linear_trend_timewise"
    input_types = [Numeric, DatetimeTimeIndex]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, attr):
        self.attr = attr

    def get_function(self):
        def function(numeric, time):
            numeric.index = time.values
            param = [{'attr': self.attr}]
            values = linear_trend_timewise(numeric, param)
            return values[0][1]

        return function
