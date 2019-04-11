from tsfresh.feature_extraction.feature_calculators import count_below_mean

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class CountBelowMean(AggregationPrimitive):
    """
    Returns the number of values in x that are lower than the mean of x
    """
    name = "count_below_mean"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return count_below_mean
