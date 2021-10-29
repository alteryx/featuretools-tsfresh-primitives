from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import (
    sum_of_reoccurring_data_points,
)
from woodwork.column_schema import ColumnSchema


class SumOfReoccurringDataPoints(AggregationPrimitive):
    """Returns the sum of all data points, that are present in the time series
    more than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.sum_of_reoccurring_data_points
    """

    name = "sum_of_reoccurring_data_points"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return sum_of_reoccurring_data_points
