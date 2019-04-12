from tsfresh.feature_extraction.feature_calculators import last_location_of_minimum

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class LastLocationOfMinimum(AggregationPrimitive):
    """
    Returns the last location of the minimal value of x.
    The position is calculated relatively to the length of x.
    """
    name = "last_location_of_minimum"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return last_location_of_minimum
