from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import ar_coefficient
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class ArCoefficient(AggregationPrimitive):
    """This feature calculator fits the unconditional maximum likelihood of an
    autoregressive AR(k) process.

    Args:
        coeff (int) : Index of returned coefficient.
        k (int) : Maximum lag of the process.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.ar_coefficient
    """

    name = "ar_coefficient"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, coeff, k):
        self.coeff = coeff
        self.k = k

    def get_function(self):
        def function(x):
            param = [{"coeff": self.coeff, "k": self.k}]
            return ar_coefficient(x, param=param)[0][1]

        return function
