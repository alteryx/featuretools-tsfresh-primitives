from tsfresh.feature_extraction.feature_calculators import minimum

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Minimum(AggregationPrimitive):
    """
    Calculates the lowest value of the time series x.
    """
    name = "minimum"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return minimum
