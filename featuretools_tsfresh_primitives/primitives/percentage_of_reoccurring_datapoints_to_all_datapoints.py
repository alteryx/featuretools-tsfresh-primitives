from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import (
    percentage_of_reoccurring_datapoints_to_all_datapoints,
)
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class PercentageOfReoccurringDatapointsToAllDatapoints(AggregationPrimitive):
    """Returns the percentage of unique values, that are present in the time
    series more than once.

        len(different values occurring more than once) / len(different values)

    This means the percentage is normalized to the number of unique values,
    in contrast to the percentage_of_reoccurring_values_to_all_values.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.percentage_of_reoccurring_datapoints_to_all_datapoints
    """

    name = "percentage_of_reoccurring_datapoints_to_all_datapoints"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return percentage_of_reoccurring_datapoints_to_all_datapoints
