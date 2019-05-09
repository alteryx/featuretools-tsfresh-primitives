from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import partial_autocorrelation


class PartialAutocorrelation(AggregationPrimitive):
    """Calculates the value of the partial autocorrelation function at
    the given lag. The lag `k` partial autocorrelation of a time series
    :math:`\\lbrace x_t, t = 1 \\ldots T \\rbrace` equals the partial
    correlation of :math:`x_t` and :math:`x_{t-k}`, adjusted for the
    intermediate variables
    :math:`\\lbrace x_{t-1}, \\ldots, x_{t-k+1} \\rbrace` ([1]).
    Following [2], it can be defined as

    .. math::

        \\alpha_k = \\frac{ Cov(x_t, x_{t-k} | x_{t-1}, \\ldots, x_{t-k+1})}
        {\\sqrt{ Var(x_t | x_{t-1}, \\ldots, x_{t-k+1}) Var(x_{t-k} | x_{t-1}, \\ldots, x_{t-k+1} )}}

    with (a) :math:`x_t = f(x_{t-1}, \\ldots, x_{t-k+1})` and (b)
    :math:`x_{t-k} = f(x_{t-1}, \\ldots, x_{t-k+1})` being AR(k-1) models that
    can be fitted by OLS. Be aware that in (a), the regression is done on past
    values to predict :math:`x_t` whereas in (b), future values are used to
    calculate the past value :math:`x_{t-k}`. It is said in [1] that "for an
    AR(p), the partial autocorrelations [ :math:`\\alpha_k` ] will be nonzero
    for `k<=p` and zero for `k>p`." With this property, it is used to determine
    the lag of an AR-Process.

    .. rubric:: References

    |  [1] Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015).
    |  Time series analysis: forecasting and control. John Wiley & Sons.
    |  [2] https://onlinecourses.science.psu.edu/stat510/node/62

    Args:
        lag (int) : The lag to be returned.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.partial_autocorrelation
    """
    name = "partial_autocorrelation"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, lag):
        self.lag = lag

    def get_function(self):
        def function(x):
            param = [{'lag': self.lag}]
            return partial_autocorrelation(x, param=param)[0][1]

        return function
