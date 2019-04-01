from tsfresh.feature_extraction.feature_calculators import agg_linear_trend

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class AggLinearTrend(AggregationPrimitive):
    '''
    Calculates a linear least-squares regression for values of the time series that were aggregated over chunks versus the sequence from 0 up to the number of chunks minus one.

    Args:
        attr (str) : Controls which of the characteristics are returned.
            Possible extracted attributes are: ['pvalue', 'rvalue', 'intercept', 'slope', 'stderr'].
        chunk_len (int) : Specifies how many time series values are in each chunk.
        f_agg (str) : Name of the aggregator function. Possible values are: [ 'max', 'min' or , 'mean', 'median'].
    '''
    name = "agg_linear_trend"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, attr, chunk_len, f_agg):
        self.attr = attr
        self.chunk_len = chunk_len
        self.f_agg = f_agg

    def get_function(self):
        def function(x):
            param = [{'attr': self.attr, 'f_agg': self.f_agg, 'chunk_len': self.chunk_len}]
            return list(agg_linear_trend(x, param))[0][1]

        return function

    def generate_name(self, base_feature_names, child_entity_id, parent_entity_id, where_str, use_prev_str):
        names = ", ".join(base_feature_names)
        parameter_to_string = lambda parameter: '{}={}'.format(parameter, getattr(self, parameter))
        parameters = ', '.join(map(parameter_to_string, ['attr', 'chunk_len', 'f_agg']))
        return u"%s(%s.%s%s%s, %s)" % (self.name.upper(), child_entity_id, names, where_str, use_prev_str, parameters)
