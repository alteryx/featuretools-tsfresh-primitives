from tsfresh.feature_extraction.feature_calculators import median

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Median(AggregationPrimitive):
    """
    Returns the median of x.
    """
    name = "median"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return median
