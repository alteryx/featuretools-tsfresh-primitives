from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import standard_deviation
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class StandardDeviation(AggregationPrimitive):
    """Returns the standard deviation of x

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.standard_deviation
    """

    name = "standard_deviation"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return standard_deviation
