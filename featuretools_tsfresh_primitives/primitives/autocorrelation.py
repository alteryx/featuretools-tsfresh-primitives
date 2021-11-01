from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import autocorrelation
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class Autocorrelation(AggregationPrimitive):
    """Calculates the autocorrelation of the specified lag.

    Args:
        lag (int) : The lag.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.autocorrelation
    """

    name = "autocorrelation"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, lag):
        self.lag = lag

    def get_function(self):
        def function(x):
            return autocorrelation(x, lag=self.lag)

        return function
