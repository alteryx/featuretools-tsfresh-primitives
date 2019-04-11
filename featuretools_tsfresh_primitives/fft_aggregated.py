from tsfresh.feature_extraction.feature_calculators import fft_aggregated

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class FftAggregated(AggregationPrimitive):
    """
    Returns the spectral centroid (mean), variance, skew, and kurtosis of the absolute fourier transform spectrum.

    Args:
        aggtype (str) : Controls which aggregation is returned.
            Possible values are: ["centroid", "variance", "skew", "kurtosis"]
    """
    name = "fft_aggregated"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, aggtype):
        self.aggtype = aggtype

    def get_function(self):
        def function(x):
            param = [{'aggtype': self.aggtype}]
            return list(fft_aggregated(x, param=param))[0][1]

        return function
