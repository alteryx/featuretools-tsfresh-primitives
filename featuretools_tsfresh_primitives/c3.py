from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import c3


class C3(AggregationPrimitive):
    """This function calculates the value of

    .. math::

        \\frac{1}{n-2lag} \\sum_{i=0}^{n-2lag} x_{i + 2 \\cdot lag}^2 \\cdot x_{i + lag} \\cdot x_{i}

    which is

    .. math::

        \\mathbb{E}[L^2(X)^2 \\cdot L(X) \\cdot X]

    where :math:`\\mathbb{E}` is the mean and :math:`L` is the lag operator.
    It was proposed in [1] as a measure of non linearity in the time series.

    .. rubric:: References

    |  [1] Schreiber, T. and Schmitz, A. (1997).
    |  Discrimination power of measures for nonlinearity in a time series
    |  PHYSICAL REVIEW E, VOLUME 55, NUMBER 5

    Args:
        lag (int) : The lag that should be used in the calculation of the feature.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.c3
    """
    name = "c3"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, lag):
        self.lag = lag

    def get_function(self):
        def function(x):
            return c3(x, lag=self.lag)

        return function
