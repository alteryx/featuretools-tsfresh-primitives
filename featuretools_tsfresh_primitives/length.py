from tsfresh.feature_extraction.feature_calculators import length

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Length(AggregationPrimitive):
    """
    Returns the length of x.
    """
    name = "length"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return length
