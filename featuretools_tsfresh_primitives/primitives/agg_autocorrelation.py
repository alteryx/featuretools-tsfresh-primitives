from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import agg_autocorrelation
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class AggAutocorrelation(AggregationPrimitive):
    """Calculates the value of an aggregation function (e.g. the variance or
    the mean) over the autocorrelation for different lags.

    Args:
        f_agg (str) : Name of a numpy function (e.g. "mean", "var", "std",
            "median"), its the name of the aggregator function that is applied
            to the autocorrelations.
        maxlag (int) : Maximal number of lags to consider.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.agg_autocorrelation
    """

    name = "agg_autocorrelation"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, f_agg, maxlag):
        self.f_agg = f_agg
        self.maxlag = maxlag

    def get_function(self):
        def function(x):
            param = [{"f_agg": self.f_agg, "maxlag": self.maxlag}]
            return agg_autocorrelation(x, param=param)[0][1]

        return function
