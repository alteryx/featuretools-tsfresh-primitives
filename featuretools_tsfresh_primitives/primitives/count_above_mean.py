from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import count_above_mean
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import IntegerNullable
# --> docs say float but if its just counting it should be int?


class CountAboveMean(AggregationPrimitive):
    """Returns the number of values in x that are higher than the mean of x

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.count_above_mean
    """
    name = "count_above_mean"
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(semantic_tags={'numeric'})
    stack_on_self = False

    def get_function(self):
        return count_above_mean
