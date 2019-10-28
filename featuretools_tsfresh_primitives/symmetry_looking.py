from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Boolean, Numeric
from tsfresh.feature_extraction.feature_calculators import symmetry_looking


class SymmetryLooking(AggregationPrimitive):
    """Boolean variable denoting if the distribution looks symmetric.

    Args:
        r (float) : Percentage of the range to compare with.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.symmetry_looking
    """
    name = "symmetry_looking"
    input_types = [Numeric]
    return_type = Boolean
    stack_on_self = False

    def __init__(self, r):
        self.r = r

    def get_function(self):
        def function(x):
            param = [{'r': self.r}]
            return symmetry_looking(x, param)[0][1]

        return function
