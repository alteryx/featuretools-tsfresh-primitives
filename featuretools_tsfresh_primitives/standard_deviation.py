from tsfresh.feature_extraction.feature_calculators import standard_deviation

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class StandardDeviation(AggregationPrimitive):
    """
    Returns the standard deviation of x
    """
    name = "standard_deviation"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return standard_deviation
