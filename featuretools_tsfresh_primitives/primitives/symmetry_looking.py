from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import symmetry_looking
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class SymmetryLooking(AggregationPrimitive):
    """Boolean column denoting if the distribution looks symmetric.

    Args:
        r (float) : Percentage of the range to compare with.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.symmetry_looking
    """

    name = "symmetry_looking"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def __init__(self, r):
        self.r = r

    def get_function(self):
        def function(x):
            param = [{"r": self.r}]
            return symmetry_looking(x, param)[0][1]

        return function
