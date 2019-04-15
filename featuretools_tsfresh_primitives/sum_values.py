from tsfresh.feature_extraction.feature_calculators import sum_values

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class SumValues(AggregationPrimitive):
    """
    Calculates the sum over the time series values.
    """
    name = "sum_values"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return sum_values
