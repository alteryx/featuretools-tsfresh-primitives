from tsfresh.feature_extraction.feature_calculators import agg_autocorrelation

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class AggAutocorrelation(AggregationPrimitive):
    '''
    Calculates the value of an aggregation function (e.g. the variance or the mean) over the autocorrelation for different lags.

    Args:
        f_agg (str) : Name of a numpy function (e.g. "mean", "var", "std", "median"), its the name of the aggregator function that is applied to the autocorrelations.
        maxlag (int) : Maximal number of lags to consider.
    '''
    name = "agg_autocorrelation"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def __init__(self, f_agg, maxlag):
        self.f_agg = f_agg
        self.maxlag = maxlag

    def get_function(self):
        def function(x):
            param = [{'f_agg': self.f_agg, 'maxlag': self.maxlag}]
            return agg_autocorrelation(x, param=param)[0][1]

        return function

    def generate_name(self, base_feature_names, child_entity_id, parent_entity_id, where_str, use_prev_str):
        names = ", ".join(base_feature_names)
        parameter_to_string = lambda parameter: '{}={}'.format(parameter, getattr(self, parameter))
        parameters = ', '.join(map(parameter_to_string, ['f_agg', 'maxlag']))
        return u"%s(%s.%s%s%s, %s)" % (self.name.upper(), child_entity_id, names, where_str, use_prev_str, parameters)
