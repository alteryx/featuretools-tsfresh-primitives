from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import mean_change
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class MeanChange(AggregationPrimitive):
    """Returns the mean over the differences between subsequent time series
    values which is

    .. math::

        \\frac{1}{n} \\sum_{i=1,\\ldots, n-1}  x_{i+1} - x_{i}

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.mean_change
    """

    name = "mean_change"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return mean_change
