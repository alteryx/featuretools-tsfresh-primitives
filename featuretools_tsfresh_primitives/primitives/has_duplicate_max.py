from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Boolean, Numeric
from tsfresh.feature_extraction.feature_calculators import has_duplicate_max
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class HasDuplicateMax(AggregationPrimitive):
    """Checks if the maximum value of x is observed more than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.has_duplicate_max
    """
    name = "has_duplicate_max"
    input_types = [Numeric]
    return_type = Boolean
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def get_function(self):
        return has_duplicate_max
