from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import mean_abs_change


class MeanAbsChange(AggregationPrimitive):
    """Returns the mean over the absolute differences between subsequent time
    series values which is

    .. math::

        \\frac{1}{n} \\sum_{i=1,\\ldots, n-1} | x_{i+1} - x_{i}|

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.mean_abs_change
    """
    name = "mean_abs_change"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return mean_abs_change
