from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import max_langevin_fixed_point


class MaxLangevinFixedPoint(AggregationPrimitive):
    """Largest fixed point of dynamics :math:argmax_x {h(x)=0}` estimated from
    polynomial :math:`h(x)`, which has been fitted to the deterministic
    dynamics of Langevin model

    .. math::
        \\dot(x)(t) = h(x(t)) + R \\mathcal(N)(0,1)

    as described by

        Friedrich et al. (2000): Physics Letters A 271, p. 217-222
        *Extracting model equations from experimental data*

    For short time-series this method is highly dependent on the parameters.

    Args:
        m (int) : Order of polynomial to fit for estimating fixed points of dynamics.
        r (float) : Number of quantils to use for averaging.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.max_langevin_fixed_point
    """
    name = "max_langevin_fixed_point"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, m, r):
        self.m = m
        self.r = r

    def get_function(self):
        def function(x):
            return max_langevin_fixed_point(x, m=self.m, r=self.r)

        return function
