from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import range_count


class RangeCount(AggregationPrimitive):
    """Count observed values within the interval [min, max).

    Args:
        min (float) : The inclusive lower bound of the range.
        max (float) : The exclusive upper bound of the range.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.range_count
    """
    name = "range_count"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_function(self):
        def function(x):
            return range_count(x, min=self.min, max=self.max)

        return function
