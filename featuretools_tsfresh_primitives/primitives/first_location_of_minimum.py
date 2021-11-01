from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import first_location_of_minimum
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class FirstLocationOfMinimum(AggregationPrimitive):
    """Returns the first location of the minimal value of x. The position is
    calculated relatively to the length of x.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.first_location_of_minimum
    """

    name = "first_location_of_minimum"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        def function(x):
            return first_location_of_minimum(x.to_numpy())

        return function
