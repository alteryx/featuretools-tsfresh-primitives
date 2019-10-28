from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import number_peaks


class NumberPeaks(AggregationPrimitive):
    """Calculates the number of peaks of at least support n in the time series
    x. A peak of support n is defined as a subsequence of x where a value
    occurs, which is bigger than its n neighbours to the left and to the right.

    Hence in the sequence

    >>> x = [3, 0, 0, 4, 0, 0, 13]

    4 is a peak of support 1 and 2 because in the subsequences

    >>> [0, 4, 0]
    >>> [0, 0, 4, 0, 0]

    4 is still the highest value. Here, 4 is not a peak of support 3 because 13
    is the 3th neighbour to the right of 4 and its bigger than 4.

    Args:
        n (int) : The support of the peak.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.number_peaks
    """
    name = "number_peaks"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, n):
        self.n = n

    def get_function(self):
        def function(x):
            return number_peaks(x, n=self.n)

        return function
