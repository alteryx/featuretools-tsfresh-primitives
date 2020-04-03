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
    """Creates a mapping for primitive instances from a dictionary list of parameters.

        Args:
            fc_parameters (ComprehensiveFCParameters): An instance of :class:`ComprehensiveFCParameters`

        Returns:
            dict: A dictionary where the keys are the names of the primitives
                and the values are lists of primitive instances.

        Examples:

            >>> parameters = {'autocorrelation': [{'lag': 2}]}
            >>> primitives = comprehensive_primitives(parameters)
            >>> primitive = primitives['autocorrelation'][0]
            >>> primitive(range(3))
            -1.5
    """
    parameters = fc_parameters or ComprehensiveFCParameters()
    agg_primitives = {}

    def append(primitive, primitives):
        inputs = parameters[primitive.name] or [{}]
        primitives[primitive.name] = []

        for values in inputs:
            instance = primitive(**values)
            primitives[primitive.name].append(instance)

    for primitive in supported_primitives():
        if primitive.name not in parameters: continue

        else:
            assert issubclass(primitive, AggregationPrimitive)
            append(primitive, agg_primitives)

    return agg_primitives
