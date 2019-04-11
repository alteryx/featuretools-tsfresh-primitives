from tsfresh.feature_extraction.feature_calculators import spkt_welch_density

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class SpktWelchDensity(AggregationPrimitive):
    """
    This feature calculator estimates the cross power spectral density of the time series at different frequencies.
    To do so, the time series is first shifted from the time domain to the frequency domain.

    Args:
        coeff (int) : Value of coefficient.
    """
    name = "spkt_welch_density"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, coeff):
        self.coeff = coeff

    def get_function(self):
        def function(x):
            param = [{'coeff': self.coeff}]
            return list(spkt_welch_density(x, param))[0][1]

        return function
