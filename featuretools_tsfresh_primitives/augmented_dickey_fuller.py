from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import augmented_dickey_fuller


class AugmentedDickeyFuller(AggregationPrimitive):
    """The Augmented Dickey-Fuller test is a hypothesis test which checks
    whether a unit root is present in a time series sample.

    Args:
        attr (str) : Controls which attribute is returned. Possible values are:
            ['pvalue', 'teststat', 'usedlag'].

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.augmented_dickey_fuller
    """
    name = "augmented_dickey_fuller"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, attr):
        self.attr = attr

    def get_function(self):
        def function(x):
            param = [{'attr': self.attr}]
            return augmented_dickey_fuller(x, param=param)[0][1]

        return function
