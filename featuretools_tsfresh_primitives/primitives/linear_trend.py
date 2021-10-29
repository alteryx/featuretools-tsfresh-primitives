from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import linear_trend
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class LinearTrend(AggregationPrimitive):
    """Calculate a linear least-squares regression for the values of the time
    series versus the sequence from 0 to length of the time series minus one.
    This feature assumes the signal to be uniformly sampled. It will not use
    the time stamps to fit the model.

    Args:
        attr (str) : Controls which of the characteristics are returned.
            Possible extracted attributes are:
                ['pvalue', 'rvalue', 'intercept', 'slope', 'stderr'].

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.linear_trend
    """

    name = "linear_trend"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, attr):
        self.attr = attr

    def get_function(self):
        def function(x):
            param = [{"attr": self.attr}]
            return list(linear_trend(x, param))[0][1]

        return function
