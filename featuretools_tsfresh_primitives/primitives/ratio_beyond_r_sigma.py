from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import ratio_beyond_r_sigma
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class RatioBeyondRSigma(AggregationPrimitive):
    """Ratio of values that are more than r*std(x) (so r sigma) away from the
    mean of x.

    Args:
        r (float) : Weight of sigma.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.ratio_beyond_r_sigma
    """

    name = "ratio_beyond_r_sigma"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, r):
        self.r = r

    def get_function(self):
        def function(x):
            return ratio_beyond_r_sigma(x, r=self.r)

        return function
