from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import count_below
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class CountBelow(AggregationPrimitive):
    """Returns the percentage of values in x that are lower than t

        Args:
            t (float) : value used as threshold

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.count_below
    """

    name = "count_below"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, t):
        self.t = t

    def get_function(self):
        def function(x):
            return count_below(x, self.t)

        return function
