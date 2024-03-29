from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import (
    variance_larger_than_standard_deviation,
)
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class VarianceLargerThanStandardDeviation(AggregationPrimitive):
    """Boolean column denoting if the variance of x is greater than its
    standard deviation. Is equal to variance of x being larger than 1

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.variance_larger_than_standard_deviation
    """

    name = "variance_larger_than_standard_deviation"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def get_function(self):
        return variance_larger_than_standard_deviation
