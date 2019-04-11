from tsfresh.feature_extraction.feature_calculators import autocorrelation

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class Autocorrelation(AggregationPrimitive):
    '''
    Calculates the autocorrelation of the specified lag.

    Args:
        lag (int) : The lag.
    '''
    name = "autocorrelation"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, lag):
        self.lag = lag

    def get_function(self):
        def function(x):
            return autocorrelation(x, lag=self.lag)

        return function
