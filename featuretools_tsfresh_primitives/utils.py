from featuretools.primitives import AggregationPrimitive, TransformPrimitive
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

import featuretools_tsfresh_primitives


def supported_primitives():
    types = AggregationPrimitive, TransformPrimitive
    for key in dir(featuretools_tsfresh_primitives):
        value = getattr(featuretools_tsfresh_primitives, key)
        is_primitive = isinstance(value, type) and issubclass(value, types)
        if is_primitive: yield value


def comprehensive_primitives(fc_parameters=None):
    parameters = fc_parameters or ComprehensiveFCParameters()
    agg_primitives, trans_primitives = {}, {}

    def append(primitive, primitives):
        inputs = parameters[primitive.name] or [{}]
        primitives[primitive.name] = []

        for values in inputs:
            instance = primitive(**values)
            primitives[primitive.name].append(instance)

    for primitive in supported_primitives():
        if primitive.name not in parameters: continue

        elif issubclass(primitive, AggregationPrimitive):
            append(primitive, agg_primitives)

        else:
            assert issubclass(primitive, TransformPrimitive)
            append(primitive, trans_primitives)

    return agg_primitives, trans_primitives
