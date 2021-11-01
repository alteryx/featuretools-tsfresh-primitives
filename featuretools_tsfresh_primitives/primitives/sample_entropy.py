from featuretools.primitives import AggregationPrimitive
from tsfresh.feature_extraction.feature_calculators import sample_entropy
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import Double


class SampleEntropy(AggregationPrimitive):
    """Calculate and return sample entropy of x.

    .. rubric:: References

    |  [1] http://en.wikipedia.org/wiki/Sample_Entropy
    |  [2] https://www.ncbi.nlm.nih.gov/pubmed/10843903?dopt=Abstract

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.sample_entropy
    """

    name = "sample_entropy"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=Double, semantic_tags={"numeric"})
    stack_on_self = False

    def get_function(self):
        return sample_entropy
