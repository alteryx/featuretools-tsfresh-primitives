from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import has_duplicate_min
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class HasDuplicateMin(AggregationPrimitive):
    """Checks if the minimal value of x is observed more than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.has_duplicate_min
    """

    name = "has_duplicate_min"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def get_function(self):
        return has_duplicate_min
