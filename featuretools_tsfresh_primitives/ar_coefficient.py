from tsfresh.feature_extraction.feature_calculators import ar_coefficient

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class ArCoefficient(AggregationPrimitive):
    '''
    This feature calculator fits the unconditional maximum likelihood of an autoregressive AR(k) process.

    Args:
        coeff (int) : Index of returned coefficient.
        k (int) : Maximum lag of the process.
    '''
    name = "ar_coefficient"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, coeff, k):
        self.coeff = coeff
        self.k = k

    def get_function(self):
        def function(x):
            param = [{'coeff': self.coeff, 'k': self.k}]
            return ar_coefficient(x, param=param)[0][1]

        return function
