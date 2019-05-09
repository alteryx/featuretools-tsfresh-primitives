from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import absolute_sum_of_changes


class AbsoluteSumOfChanges(AggregationPrimitive):
    """Returns the sum over the absolute value
    of consecutive changes in the series x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.absolute_sum_of_changes
    """
    name = "absolute_sum_of_changes"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return absolute_sum_of_changes
