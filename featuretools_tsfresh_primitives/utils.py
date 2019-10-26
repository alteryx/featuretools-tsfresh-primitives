import importlib


def _camel_case(snake_str):
    words = snake_str.split('_')
    titled_words = map(str.title, words)
    return ''.join(titled_words)


def _tsfresh_to_featuretools(fc_name):
    module = importlib.import_module('featuretools_tsfresh_primitives')
    return getattr(module, _camel_case(fc_name))


def primitives_from_fc_settings(fc_settings):
    """
    Return a list of :class:AggregationPrimitive from tsfresh settings.
    The format is the same as the argument `default_fc_parameters` of
    :func:`tsfresh.feature_extraction.extract_features`

    Args:
        fc_settings (dict): mapping from tsfresh feature calculator names (snake case) to parameters.
            Only those names which are keys in this dict will be calculated.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#module-tsfresh
    .feature_extraction.settings
    """
    primitives = []
    for fc_name, params_list in fc_settings.items():
        if not isinstance(params_list, list):
            params_list = [params_list]
        primitive_cls = _tsfresh_to_featuretools(fc_name)
        fc_primitives = [primitive_cls(**params or {}) for params in params_list]
        primitives.extend(fc_primitives)
    return primitives
