from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import longest_strike_above_mean


class LongestStrikeAboveMean(AggregationPrimitive):
    """Returns the length of the longest consecutive subsequence in x that is
    bigger than the mean of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.longest_strike_above_mean
    """
    name = "longest_strike_above_mean"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return longest_strike_above_mean
