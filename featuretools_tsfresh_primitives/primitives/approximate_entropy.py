from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import approximate_entropy


class ApproximateEntropy(AggregationPrimitive):
    """Implements a vectorized Approximate entropy algorithm.

    Args:
        m (int) : Length of compared run of data.
        r (float) : Filtering level, must be positive.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.approximate_entropy
    """
    name = "approximate_entropy"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, m, r):
        self.m = m
        self.r = r

    def get_function(self):
        def function(x):
            return approximate_entropy(x, m=self.m, r=self.r)

        return function
