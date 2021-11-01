from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import minimum
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class Minimum(AggregationPrimitive):
    """Calculates the lowest value of the time series x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.minimum
    """

    name = "minimum"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return minimum
