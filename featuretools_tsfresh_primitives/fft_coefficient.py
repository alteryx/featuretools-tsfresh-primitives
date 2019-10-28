from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import fft_coefficient


class FftCoefficient(AggregationPrimitive):
    """Calculates the fourier coefficients of the one-dimensional discrete
    Fourier Transform for real input by fast fourier transformation algorithm

    .. math::
        A_k =  \\sum_{m=0}^{n-1} a_m \\exp \\left \\{ -2 \\pi i \\frac{m k}{n} \\right \\}, \\qquad k = 0,
        \\ldots , n-1.

    The resulting coefficients will be complex, this feature calculator can
    return the real part (attr=="real"), the imaginary part (attr=="imag), the
    absolute value (attr=""abs) and the angle in degrees (attr=="angle).

    Args:
        coeff (int) : The coefficient to return. Must be greater than or equal to zero.
        attr (str) : Controls which attribute is returned.
            Possible values are: ["real", "imag", "abs", "angle"]

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.fft_coefficient
    """
    name = "fft_coefficient"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, coeff, attr):
        self.coeff = coeff
        self.attr = attr

    def get_function(self):
        def function(x):
            param = [{'coeff': self.coeff, 'attr': self.attr}]
            return list(fft_coefficient(x, param=param))[0][1]

        return function
