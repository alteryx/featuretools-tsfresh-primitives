from tsfresh.feature_extraction.feature_calculators import sum_of_reoccurring_data_points

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class SumOfReoccurringDataPoints(AggregationPrimitive):
    """
    Returns the sum of all data points, that are present in the time series
    more than once.
    """
    name = "sum_of_reoccurring_data_points"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return sum_of_reoccurring_data_points
