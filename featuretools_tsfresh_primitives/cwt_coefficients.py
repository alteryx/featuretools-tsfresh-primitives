from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import cwt_coefficients


class CwtCoefficients(AggregationPrimitive):
    """Calculates a Continuous wavelet transform for the Ricker wavelet, also
    known as the "Mexican hat wavelet" which is defined by

    .. math::
        \\frac{2}{\\sqrt{3a} \\pi^{\\frac{1}{4}}} (1 - \\frac{x^2}{a^2}) exp(-\\frac{x^2}{2a^2})

    where :math:`a` is the width parameter of the wavelet function.

    This feature calculator takes three different parameter: widths, coeff and
    w. The feature calculater takes all the different widths arrays and then
    calculates the cwt one time for each different width array. Then the values
    for the different coefficient for coeff and width w are returned.

    Args:
        widths (list[int]) : The different widths arrays.
        coeff (int) : The different coefficient to return.
        w (int) : The different width to return.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.cwt_coefficients
    """
    name = "cwt_coefficients"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, widths, coeff, w):
        self.widths = tuple(widths)
        self.coeff = coeff
        self.w = w

    def get_function(self):
        def function(x):
            param = [{'widths': self.widths, 'coeff': self.coeff, 'w': self.w}]
            return list(cwt_coefficients(x, param=param))[0][1]

        return function
