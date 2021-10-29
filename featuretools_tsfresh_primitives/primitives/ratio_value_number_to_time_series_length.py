from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import (
    ratio_value_number_to_time_series_length,
)
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class RatioValueNumberToTimeSeriesLength(AggregationPrimitive):
    """Returns a factor which is 1 if all values in the time series occur only
    once, and below one if this is not the case. In principle, it just returns

        # unique values / # values

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.ratio_value_number_to_time_series_length
    """

    name = "ratio_value_number_to_time_series_length"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return ratio_value_number_to_time_series_length
