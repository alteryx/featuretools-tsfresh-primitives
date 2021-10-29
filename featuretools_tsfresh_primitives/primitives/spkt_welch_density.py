from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import spkt_welch_density
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class SpktWelchDensity(AggregationPrimitive):
    """This feature calculator estimates the cross power spectral density of
    the time series at different frequencies. To do so, the time series is
    first shifted from the time domain to the frequency domain.

    Args:
        coeff (int) : Value of coefficient.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.spkt_welch_density
    """

    name = "spkt_welch_density"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, coeff):
        self.coeff = coeff

    def get_function(self):
        def function(x):
            param = [{"coeff": self.coeff}]
            return list(spkt_welch_density(x, param))[0][1]

        return function
