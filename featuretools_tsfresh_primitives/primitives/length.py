from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import length
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import IntegerNullable


class Length(AggregationPrimitive):
    """Returns the length of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.length
    """
    name = "length"
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(semantic_tags={'numeric'})
    stack_on_self = False

    def get_function(self):
        return length
