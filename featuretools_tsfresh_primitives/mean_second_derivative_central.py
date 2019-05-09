from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import mean_second_derivative_central


class MeanSecondDerivativeCentral(AggregationPrimitive):
    """Returns the mean value of a central approximation
    of the second derivative

    .. math::

        \\frac{1}{n} \\sum_{i=1,\\ldots, n-1}  \\frac{1}{2} (x_{i+2} - 2 \\cdot x_{i+1} + x_i)

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.mean_second_derivative_central
    """
    name = "mean_second_derivative_central"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return mean_second_derivative_central
