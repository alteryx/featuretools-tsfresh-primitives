from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import cid_ce


class CidCe(AggregationPrimitive):
    """This function calculator is an estimate for a time series complexity [1]
    (A more complex time series has more peaks, valleys etc.). It calculates
    the value of

    .. math::

        \\sqrt{ \\sum_{i=0}^{n-2lag} ( x_{i} - x_{i+1})^2 }

    .. rubric:: References

    |  [1] Batista, Gustavo EAPA, et al (2014).
    |  CID: an efficient complexity-invariant distance for time series.
    |  Data Mining and Knowledge Discovery 28.3 (2014): 634-669.

    Args:
        normalize (bool) : Should the time series be z-transformed?

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.cid_ce
    """
    name = "cid_ce"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, normalize):
        self.normalize = normalize

    def get_function(self):
        def function(x):
            return cid_ce(x, normalize=self.normalize)

        return function
