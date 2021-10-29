from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import index_mass_quantile
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class IndexMassQuantile(AggregationPrimitive):
    """Those apply features calculate the relative index i where q% of the mass
    of the time series x lie left of i. For example for q = 50% this feature
    calculator will return the mass center of the time series.

    Args:
        q (float) : Percentage of the mass of the time series.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.index_mass_quantile
    """

    name = "index_mass_quantile"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, q):
        self.q = q

    def get_function(self):
        def function(x):
            param = [{"q": self.q}]
            return index_mass_quantile(x, param=param)[0][1]

        return function
