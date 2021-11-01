from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import kurtosis
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class Kurtosis(AggregationPrimitive):
    """Returns the kurtosis of x (calculated with the adjusted Fisher-Pearson
    standardized moment coefficient G2).

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.kurtosis
    """

    name = "kurtosis"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return kurtosis
