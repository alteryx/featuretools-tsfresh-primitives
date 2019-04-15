from tsfresh.feature_extraction.feature_calculators import sample_entropy

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class SampleEntropy(AggregationPrimitive):
    """
    Calculate and return sample entropy of x.

    .. rubric:: References

    |  [1] http://en.wikipedia.org/wiki/Sample_Entropy
    |  [2] https://www.ncbi.nlm.nih.gov/pubmed/10843903?dopt=Abstract
    """
    name = "sample_entropy"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return sample_entropy
