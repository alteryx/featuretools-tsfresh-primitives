from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import large_standard_deviation
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable


class LargeStandardDeviation(AggregationPrimitive):
    """Boolean column denoting if the standard dev of x is higher than 'r'
    times the range = difference between max and min of x. Hence it checks if

    .. math::

        std(x) > r * (max(X)-min(X))

    According to a rule of the thumb, the standard deviation should be a forth
    of the range of the values.

    Args:
        r (float) : The percentage of the range to compare with.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.large_standard_deviation
    """

    name = "large_standard_deviation"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    stack_on_self = False

    def __init__(self, r):
        self.r = r

    def get_function(self):
        def function(x):
            return large_standard_deviation(x, r=self.r)

        return function
