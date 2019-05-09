from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric
from tsfresh.feature_extraction.feature_calculators import energy_ratio_by_chunks


class EnergyRatioByChunks(AggregationPrimitive):
    """Calculates the sum of squares of chunk i out of N chunks expressed as a
    ratio with the sum of squares over the whole series.

    Args:
        num_segments (int) : Number of segments to divide the series into.
        segment_focus (int) : Segment number (starting at zero) to return a feature on.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.energy_ratio_by_chunks
    """
    name = "energy_ratio_by_chunks"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, num_segments, segment_focus):
        self.num_segments = num_segments
        self.segment_focus = segment_focus

    def get_function(self):
        def function(x):
            param = [{'num_segments': self.num_segments, 'segment_focus': self.segment_focus}]
            return energy_ratio_by_chunks(x, param)[0][1]

        return function
