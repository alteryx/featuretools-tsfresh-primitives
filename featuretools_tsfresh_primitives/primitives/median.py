from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import median
from woodwork.column_schema import ColumnSchema


class Median(AggregationPrimitive):
    """Returns the median of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.median
    """
    name = "median"
    input_types = [ColumnSchema(semantic_tags={'numeric'})]
    return_type = ColumnSchema(semantic_tags={'numeric'})
    stack_on_self = False

    def get_function(self):
        return median
