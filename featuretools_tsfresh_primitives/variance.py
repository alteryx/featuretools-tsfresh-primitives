from tsfresh.feature_extraction.feature_calculators import variance

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Variance(AggregationPrimitive):
    """
    Returns the variance of x.
    """
    name = "variance"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return variance
