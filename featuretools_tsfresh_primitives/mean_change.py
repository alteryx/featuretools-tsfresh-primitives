from tsfresh.feature_extraction.feature_calculators import mean_change

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class MeanChange(AggregationPrimitive):
    """
    Returns the mean over the differences between subsequent time series values which is

    .. math::

        \\frac{1}{n} \\sum_{i=1,\\ldots, n-1}  x_{i+1} - x_{i}
    """
    name = "mean_change"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return mean_change
