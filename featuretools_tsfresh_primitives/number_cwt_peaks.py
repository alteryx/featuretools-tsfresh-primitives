from tsfresh.feature_extraction.feature_calculators import number_cwt_peaks

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class NumberCwtPeaks(AggregationPrimitive):
    """
    This feature calculator searches for different peaks in x. To do so, x is smoothed by a ricker wavelet and for
    widths ranging from 1 to n. This feature calculator returns the number of peaks that occur at enough width scales
    and with sufficiently high Signal-to-Noise-Ratio (SNR).

    Args:
        n (int) : Maximum width to consider.
    """
    name = "number_cwt_peaks"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, n):
        self.n = n

    def get_function(self):
        def function(x):
            return number_cwt_peaks(x, n=self.n)

        return function
