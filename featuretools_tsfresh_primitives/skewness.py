from tsfresh.feature_extraction.feature_calculators import skewness

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Skewness(AggregationPrimitive):
    """
    Returns the sample skewness of x (calculated with the adjusted Fisher-Pearson standardized
    moment coefficient G1).
    """
    name = "skewness"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return skewness
