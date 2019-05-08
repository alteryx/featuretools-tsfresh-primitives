from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import last_location_of_maximum


class LastLocationOfMaximum(AggregationPrimitive):
    """Returns the relative last location of the maximum value of x.
    The position is calculated relatively to the length of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.last_location_of_maximum
    """
    name = "last_location_of_maximum"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return last_location_of_maximum
