from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import friedrich_coefficients


class FriedrichCoefficients(AggregationPrimitive):
    """Coefficients of polynomial :math:`h(x)`, which has been fitted to
    the deterministic dynamics of Langevin model

    .. math::
        \\dot{x}(t) = h(x(t)) + \\mathcal{N}(0,R)

    as described by [1].

    For short time-series this method is highly dependent on the parameters.

    .. rubric:: References

    |  [1] Friedrich et al. (2000): Physics Letters A 271, p. 217-222
    |  *Extracting model equations from experimental data*

    Args:
        m (int) : The order of polynom to fit for estimating fixed points of
            dynamics. Must be a positive integer.
        r (float) : The number of quantiles to use for averaging.
        coeff (int) : The coefficient. Must be a positive interger.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.friedrich_coefficients
    """
    name = "friedrich_coefficients"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, m, r, coeff):
        self.m = m
        self.r = r
        self.coeff = coeff

    def get_function(self):
        def function(x):
            param = [{'m': self.m, 'r': self.r, 'coeff': self.coeff}]
            return list(friedrich_coefficients(x, param))[0][1]

        return function
