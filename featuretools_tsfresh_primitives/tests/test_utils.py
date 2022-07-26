from featuretools_tsfresh_primitives import (
    TSF_AGG_PRIMITIVES,
    comprehensive_fc_parameters,
    primitives_from_fc_settings,
)


def test_primitives_from_fc_settings():
    fc_parameters = comprehensive_fc_parameters()

    for primitive in TSF_AGG_PRIMITIVES:
        inputs = fc_parameters[primitive.name] or [{}]
        parameters = {primitive.name: inputs}
        instances = primitives_from_fc_settings(parameters)

        assert len(instances) == len(inputs)
        items = zip(instances, inputs)

        for instance, inputs in items:
            assert instance.name == primitive.name

            for attribute, value in inputs.items():
                assert hasattr(instance, attribute)
                assert getattr(instance, attribute) == value
