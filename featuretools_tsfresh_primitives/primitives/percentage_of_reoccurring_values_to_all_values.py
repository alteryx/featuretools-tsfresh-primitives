from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import (
    percentage_of_reoccurring_values_to_all_values,
)
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class PercentageOfReoccurringValuesToAllValues(AggregationPrimitive):
    """Returns the ratio of unique values, that are present in the time series
    more than once.

        # of data points occurring more than once / # of all data points

    This means the ratio is normalized to the number of data points in the time
    series, in contrast to the
    percentage_of_reoccurring_datapoints_to_all_datapoints.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.percentage_of_reoccurring_values_to_all_values
    """

    name = "percentage_of_reoccurring_values_to_all_values"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return percentage_of_reoccurring_values_to_all_values
