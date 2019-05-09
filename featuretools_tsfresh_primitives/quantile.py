from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import quantile


class Quantile(AggregationPrimitive):
    """Calculates the q quantile of x. This is the value of x greater than q%
    of the ordered values from x.

    Args:
        q (float) : The quantile to calculate.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.quantile
    """
    name = "quantile"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, q):
        self.q = q

    def get_function(self):
        def function(x):
            return quantile(x, q=self.q)

        return function
