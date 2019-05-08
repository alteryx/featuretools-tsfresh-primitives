from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import change_quantiles


class ChangeQuantiles(AggregationPrimitive):
    """First fixes a corridor given by the quantiles ql and qh of the
    distribution of x. Then calculates the average, absolute value of
    consecutive changes of the series x inside this corridor.

    Args:
        ql (float) : The lower quantile of the corridor.
        qh (float) : The higher quantile of the corridor.
        isabs (bool) : Should the absolute differences be taken?
        f_agg (str) : The numpy function that aggregates (e.g. mean, var, std,
            median) the differences in the bin.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.change_quantiles
    """
    name = "change_quantiles"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, ql, qh, isabs, f_agg):
        self.ql = ql
        self.qh = qh
        self.isabs = isabs
        self.f_agg = f_agg

    def get_function(self):
        def function(x):
            return change_quantiles(x,
                                    ql=self.ql,
                                    qh=self.qh,
                                    isabs=self.isabs,
                                    f_agg=self.f_agg)

        return function
