from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric, Boolean
from tsfresh.feature_extraction.feature_calculators import variance_larger_than_standard_deviation


class VarianceLargerThanStandardDeviation(AggregationPrimitive):
    """Boolean variable denoting if the variance of x is greater than its
    standard deviation. Is equal to variance of x being larger than 1

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.variance_larger_than_standard_deviation
    """
    name = "variance_larger_than_standard_deviation"
    input_types = [Numeric]
    return_type = Boolean
    stack_on_self = False

    def get_function(self):
        return variance_larger_than_standard_deviation
