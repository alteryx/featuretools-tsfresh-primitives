from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import value_count


class ValueCount(AggregationPrimitive):
    """Count occurrences of `value` in time series x.

    Args:
        value (float) : The value to be counted.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.value_count
    """
    name = "value_count"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, value):
        self.value = value

    def get_function(self):
        def function(x):
            return value_count(x, value=self.value)

        return function
