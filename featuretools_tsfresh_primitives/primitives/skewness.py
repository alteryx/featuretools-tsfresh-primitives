from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import skewness
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class Skewness(AggregationPrimitive):
    """Returns the sample skewness of x (calculated with the adjusted
    Fisher-Pearson standardized moment coefficient G1).

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.skewness
    """

    name = "skewness"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return skewness
