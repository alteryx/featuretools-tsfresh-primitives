from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import has_duplicate
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class HasDuplicate(AggregationPrimitive):
    """Checks if any value in x occurs more than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.has_duplicate
    """

    name = "has_duplicate"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def get_function(self):
        return has_duplicate
