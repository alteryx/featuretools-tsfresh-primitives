from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import \
    last_location_of_minimum
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class LastLocationOfMinimum(AggregationPrimitive):
    """Returns the last location of the minimal value of x.
    The position is calculated relatively to the length of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.last_location_of_minimum
    """
    name = "last_location_of_minimum"
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(logical_type=Double)
    stack_on_self = False

    def get_function(self):
        return last_location_of_minimum
