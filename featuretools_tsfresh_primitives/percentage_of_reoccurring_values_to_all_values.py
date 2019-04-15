from tsfresh.feature_extraction.feature_calculators import percentage_of_reoccurring_values_to_all_values

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class PercentageOfReoccurringValuesToAllValues(AggregationPrimitive):
    """
    Returns the ratio of unique values, that are present in the time series
    more than once.

        # of data points occurring more than once / # of all data points

    This means the ratio is normalized to the number of data points in the time series,
    in contrast to the percentage_of_reoccurring_datapoints_to_all_datapoints.
    """
    name = "percentage_of_reoccurring_values_to_all_values"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return percentage_of_reoccurring_values_to_all_values
