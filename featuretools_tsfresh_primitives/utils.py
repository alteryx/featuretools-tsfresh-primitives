from featuretools.primitives import AggregationPrimitive, TransformPrimitive
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

import featuretools_tsfresh_primitives


def comprehensive_fc_parameters():
    """A wrapper around the tsfresh function :class:`ComperehensiveFCParameters` to filter out unsupported parameter settings.

    Returns:
        parameters (dict) : a dictionary list of parameters

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.settings.ComprehensiveFCParameters
    """
    parameters = ComprehensiveFCParameters()

    # when a partial autocorrelation has a lag of zero,
    # an error is raised from `tsfresh.feature_extraction.extract_features`
    partial_autocorrelation = parameters['partial_autocorrelation']
    for index, values in enumerate(partial_autocorrelation):
        if values['lag'] == 0: del partial_autocorrelation[index]

    return parameters


def supported_primitives():
    """Generates the currently supported primitives.

        Returns:
            generator: primitive classes
    """
    primitive_types = AggregationPrimitive, TransformPrimitive
    for key in dir(featuretools_tsfresh_primitives):
        value = getattr(featuretools_tsfresh_primitives, key)
        is_primitive = isinstance(value, type) and issubclass(value, primitive_types)
        if is_primitive: yield value


def primitives_from_fc_settings(fc_settings=None):
    """Returns a list of :class:`AggregationPrimitive` from tsfresh settings.
    The format is the same as the argument `default_fc_parameters` of :func:`tsfresh.feature_extraction.extract_features`

    Args:
        fc_settings (dict): mapping from tsfresh feature calculator names (snake case) to parameters.
            Only those names which are keys in this dict will be calculated.
            The default value is the dictionary of parameter settings from :class:`ComperehensiveFCParameters`.

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
    parameters = fc_settings or comprehensive_fc_parameters()
    agg_primitives = []

    def add_primitive_instances(primitive, primitives):
        inputs = parameters[primitive.name] or [{}]

        for values in inputs:
            instance = primitive(**values)
            primitives.append(instance)

    for primitive in supported_primitives():
        if primitive.name in parameters:
            assert issubclass(primitive, AggregationPrimitive)
            add_primitive_instances(primitive, agg_primitives)

    return agg_primitives
