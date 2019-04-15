from tsfresh.feature_extraction.feature_calculators import ratio_value_number_to_time_series_length

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class RatioValueNumberToTimeSeriesLength(AggregationPrimitive):
    """
    Returns a factor which is 1 if all values in the time series occur only once,
    and below one if this is not the case.
    In principle, it just returns

        # unique values / # values
    """
    name = "ratio_value_number_to_time_series_length"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return ratio_value_number_to_time_series_length
