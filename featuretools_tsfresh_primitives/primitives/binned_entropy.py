from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import binned_entropy
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class BinnedEntropy(AggregationPrimitive):
    """First bins the values of x into max_bins equidistant bins.
    Then calculates the value of

    .. math::

        - \\sum_{k=0}^{min(max\\_bins, len(x))} p_k log(p_k) \\cdot \\mathbf{1}_{(p_k > 0)}

    where :math:`p_k` is the percentage of samples in bin :math:`k`.

     Args:
        max_bins (int) : The maximal number of bins.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.binned_entropy
    """

    name = "binned_entropy"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def __init__(self, max_bins):
        self.max_bins = max_bins

    def get_function(self):
        def function(x):
            return binned_entropy(x, max_bins=self.max_bins)

        return function
