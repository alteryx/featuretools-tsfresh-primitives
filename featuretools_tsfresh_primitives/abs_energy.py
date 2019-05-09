from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import abs_energy


class AbsEnergy(AggregationPrimitive):
    """Returns the absolute energy of the time series
    which is the sum over the squared values.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.abs_energy
    """
    name = "abs_energy"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return abs_energy
