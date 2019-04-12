from tsfresh.feature_extraction.feature_calculators import index_mass_quantile

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class IndexMassQuantile(AggregationPrimitive):
    """
    Those apply features calculate the relative index i where q% of the mass of the time series x lie left of i.
    For example for q = 50% this feature calculator will return the mass center of the time series.

    Args:
        q (float) : Percentage of the mass of the time series.
    """
    name = "index_mass_quantile"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, q):
        self.q = q

    def get_function(self):
        def function(x):
            param = [{'q': self.q}]
            return index_mass_quantile(x, param=param)[0][1]

        return function
