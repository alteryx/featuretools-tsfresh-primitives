from tsfresh.feature_extraction.feature_calculators import has_duplicate

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class HasDuplicate(AggregationPrimitive):
    """
    Checks if any value in x occurs more than once.
    """
    name = "has_duplicate"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return has_duplicate
