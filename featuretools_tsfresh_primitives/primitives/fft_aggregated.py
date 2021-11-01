from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import fft_aggregated
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class FftAggregated(AggregationPrimitive):
    """Returns the spectral centroid (mean), variance, skew, and kurtosis of
    the absolute fourier transform spectrum.

    Args:
        aggtype (str) : Controls which aggregation is returned. Possible values
            are: ["centroid", "variance", "skew", "kurtosis"]

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_aggregated
    """

    name = "fft_aggregated"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, aggtype):
        self.aggtype = aggtype

    def get_function(self):
        def function(x):
            param = [{"aggtype": self.aggtype}]
            return list(fft_aggregated(x, param=param))[0][1]

        return function
