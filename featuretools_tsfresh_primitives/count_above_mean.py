from tsfresh.feature_extraction.feature_calculators import count_above_mean

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class CountAboveMean(AggregationPrimitive):
    """
    Returns the number of values in x that are higher than the mean of x
    """
    name = "count_above_mean"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return count_above_mean
