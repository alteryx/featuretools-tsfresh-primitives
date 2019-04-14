from tsfresh.feature_extraction.feature_calculators import mean

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Mean(AggregationPrimitive):
    """
    Returns the mean of x.
    """
    name = "mean"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return mean
