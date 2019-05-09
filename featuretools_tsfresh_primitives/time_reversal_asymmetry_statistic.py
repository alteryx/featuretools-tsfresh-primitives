from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import time_reversal_asymmetry_statistic


class TimeReversalAsymmetryStatistic(AggregationPrimitive):
    """This function calculates the value of

    .. math::

        \\frac{1}{n-2lag} \\sum_{i=0}^{n-2lag} x_{i + 2 \\cdot lag}^2 \\cdot x_{i + lag} - x_{i + lag} \\cdot  x_{i}^2

    which is

    .. math::

        \\mathbb{E}[L^2(X)^2 \\cdot L(X) - L(X) \\cdot X^2]

    where :math:`\\mathbb{E}` is the mean and :math:`L` is the lag operator.
    It was proposed in [1] as a promising feature to extract from time series.

    .. rubric:: References

    |  [1] Fulcher, B.D., Jones, N.S. (2014).
    |  Highly comparative feature-based time-series classification.
    |  Knowledge and Data Engineering, IEEE Transactions on 26, 3026–3037.

    Args:
        lag (int) : The lag that should be used in the calculation of the feature.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.time_reversal_asymmetry_statistic
    """
    name = "time_reversal_asymmetry_statistic"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, lag):
        self.lag = lag

    def get_function(self):
        def function(x):
            return time_reversal_asymmetry_statistic(x, lag=self.lag)

        return function
