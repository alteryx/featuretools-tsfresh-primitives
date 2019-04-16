from tsfresh.feature_extraction.feature_calculators import variance_larger_than_standard_deviation

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class VarianceLargerThanStandardDeviation(AggregationPrimitive):
    """
    Returns the variance_larger_than_standard_deviation of x.
    """
    name = "variance_larger_than_standard_deviation"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return variance_larger_than_standard_deviation
