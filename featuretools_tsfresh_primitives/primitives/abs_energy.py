from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import abs_energy
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class AbsEnergy(AggregationPrimitive):
    """Returns the absolute energy of the time series
    which is the sum over the squared values.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.abs_energy
    """

    name = "abs_energy"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return abs_energy
