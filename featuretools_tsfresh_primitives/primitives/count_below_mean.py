from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import count_below_mean
from woodwork.column_schema import ColumnSchema


class CountBelowMean(AggregationPrimitive):
    """Returns the number of values in x that are lower than the mean of x

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.count_below_mean
    """
    name = "count_below_mean"
    input_types = [Numeric]
    return_type = Numeric
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(semantic_tags={'numeric'})
    stack_on_self = False

    def get_function(self):
        return count_below_mean
