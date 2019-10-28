from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric

from tsfresh.feature_extraction.feature_calculators import kurtosis


class Kurtosis(AggregationPrimitive):
    """Returns the kurtosis of x (calculated with the adjusted Fisher-Pearson
    standardized moment coefficient G2).

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.kurtosis
    """
    name = "kurtosis"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return kurtosis
