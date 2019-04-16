from tsfresh.feature_extraction.feature_calculators import variance_larger_than_standard_deviation

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric, Boolean


class VarianceLargerThanStandardDeviation(AggregationPrimitive):
    """
    Boolean variable denoting if the variance of x is greater than its standard deviation. Is equal to variance of x
    being larger than 1
    """
    name = "variance_larger_than_standard_deviation"
    input_types = [Numeric]
    return_type = Boolean
    stack_on_self = False

    def get_function(self):
        return variance_larger_than_standard_deviation
