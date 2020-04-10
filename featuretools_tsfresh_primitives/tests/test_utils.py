

from featuretools_tsfresh_primitives.utils import (comprehensive_fc_parameters,
                                                   primitives_from_fc_settings,
                                                   supported_primitives)


def test_primitives_from_fc_settings():
    fc_parameters = comprehensive_fc_parameters()

    for primitive in supported_primitives():
        inputs = fc_parameters[primitive.name] or [{}]
        paramters = {primitive.name: inputs}
        instances = primitives_from_fc_settings(paramters)

        assert len(instances) == len(inputs)
        items = zip(instances, inputs)

        for instance, inputs in items:
            assert instance.name == primitive.name

            for attribute, value in inputs.items():
                assert hasattr(instance, attribute)
                assert getattr(instance, attribute) == value
