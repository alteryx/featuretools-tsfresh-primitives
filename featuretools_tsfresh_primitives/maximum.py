from tsfresh.feature_extraction.feature_calculators import maximum

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Maximum(AggregationPrimitive):
    """
    Calculates the highest value of the time series x.
    """
    name = "maximum"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return maximum
