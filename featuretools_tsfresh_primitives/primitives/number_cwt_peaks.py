from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import number_cwt_peaks
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import IntegerNullable


class NumberCwtPeaks(AggregationPrimitive):
    """This feature calculator searches for different peaks in x. To do so, x
    is smoothed by a ricker wavelet and for widths ranging from 1 to n. This
    feature calculator returns the number of peaks that occur at enough width
    scales and with sufficiently high Signal-to-Noise-Ratio (SNR).

    Args:
        n (int) : Maximum width to consider.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.number_cwt_peaks
    """

    name = "number_cwt_peaks"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=IntegerNullable, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, n):
        self.n = n

    def get_function(self):
        def function(x):
            return number_cwt_peaks(x, n=self.n)

        return function
