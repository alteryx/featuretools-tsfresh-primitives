from tsfresh.feature_extraction.feature_calculators import ratio_beyond_r_sigma

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class RatioBeyondRSigma(AggregationPrimitive):
    """
    Ratio of values that are more than r*std(x) (so r sigma) away from the mean of x.

    Args:
        r (float) : Weight of sigma.
    """
    name = "ratio_beyond_r_sigma"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, r):
        self.r = r

    def get_function(self):
        def function(x):
            return ratio_beyond_r_sigma(x, r=self.r)

        return function
