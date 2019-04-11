from tsfresh.feature_extraction.feature_calculators import absolute_sum_of_changes

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class AbsoluteSumOfChanges(AggregationPrimitive):
    '''
    Returns the absolute energy of the time series which is the sum over the squared values.
    '''
    name = "absolute_sum_of_changes"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return absolute_sum_of_changes
