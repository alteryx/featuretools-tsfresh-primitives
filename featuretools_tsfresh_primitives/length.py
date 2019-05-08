from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import length


class Length(AggregationPrimitive):
    """Returns the length of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.length
    """
    name = "length"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return length
