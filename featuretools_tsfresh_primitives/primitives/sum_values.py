from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import sum_values
from woodwork.column_schema import ColumnSchema


class SumValues(AggregationPrimitive):
    """Calculates the sum over the time series values.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.sum_values
    """

    name = "sum_values"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return sum_values
