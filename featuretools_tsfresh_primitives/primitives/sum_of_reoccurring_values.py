from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import \
    sum_of_reoccurring_values
from woodwork.column_schema import ColumnSchema


class SumOfReoccurringValues(AggregationPrimitive):
    """Returns the sum of all values, that are present in the time series more
    than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.sum_of_reoccurring_values
    """
    name = "sum_of_reoccurring_values"
    input_types = [Numeric]
    return_type = Numeric
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(semantic_tags={'numeric'})
    stack_on_self = False

    def get_function(self):
        return sum_of_reoccurring_values
