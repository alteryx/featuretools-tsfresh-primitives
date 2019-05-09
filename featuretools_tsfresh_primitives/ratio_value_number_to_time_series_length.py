from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import ratio_value_number_to_time_series_length


class RatioValueNumberToTimeSeriesLength(AggregationPrimitive):
    """Returns a factor which is 1 if all values in the time series occur only
    once, and below one if this is not the case. In principle, it just returns

        # unique values / # values

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.ratio_value_number_to_time_series_length
    """
    name = "ratio_value_number_to_time_series_length"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return ratio_value_number_to_time_series_length
