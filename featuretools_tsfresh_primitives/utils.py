from featuretools.primitives import AggregationPrimitive, TransformPrimitive
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

import featuretools_tsfresh_primitives


def supported_primitives():
    """Generates the currently supported primitives.

        Returns:
            generator: primitive classes
    """
    types = AggregationPrimitive, TransformPrimitive
    for key in dir(featuretools_tsfresh_primitives):
        value = getattr(featuretools_tsfresh_primitives, key)
        is_primitive = isinstance(value, type) and issubclass(value, types)
        if is_primitive: yield value


def primitives_from_fc_settings(fc_settings=None):
    """Return a list of :class:AggregationPrimitive from tsfresh settings.
    The format is the same as the argument `default_fc_parameters` of :func:`tsfresh.feature_extraction.extract_features`

    Args:
        fc_settings (dict): mapping from tsfresh feature calculator names (snake case) to parameters.
            Only those names which are keys in this dict will be calculated.

    Returns:
        agg_primitives (list): A list of primitive instances.

    Examples:
        >>> parameters = {'autocorrelation': [{'lag': 2}]}
        >>> primitive = primitives_from_fc_settings(parameters)[0]
        >>> primitive(range(3))
        -1.5

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#module-tsfresh.feature_extraction.settings
    """
    parameters = fc_settings or ComprehensiveFCParameters()
    agg_primitives = []

    def append(primitive, primitives):
        inputs = parameters[primitive.name] or [{}]

        for values in inputs:
            instance = primitive(**values)
            primitives.append(instance)

    for primitive in supported_primitives():
        if primitive.name in parameters:
            assert issubclass(primitive, AggregationPrimitive)
            append(primitive, agg_primitives)

    return agg_primitives
