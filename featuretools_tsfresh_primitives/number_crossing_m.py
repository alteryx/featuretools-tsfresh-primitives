from tsfresh.feature_extraction.feature_calculators import number_crossing_m

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class NumberCrossingM(AggregationPrimitive):
    """
    Calculates the number of crossings of x on m. A crossing is defined as two sequential values where the first value
    is lower than m and the next is greater, or vice-versa. If you set m to zero, you will get the number of zero
    crossings.

    Args:
        m (float) : The threshold for the crossing.
    """
    name = "number_crossing_m"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, m):
        self.m = m

    def get_function(self):
        def function(x):
            return number_crossing_m(x, m=self.m)

        return function
