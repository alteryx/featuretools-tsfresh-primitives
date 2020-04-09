from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

from featuretools_tsfresh_primitives.utils import (primitives_from_fc_settings,
                                                   supported_primitives)


def test_comprehensive_primitives():
    fc_parameters = ComprehensiveFCParameters()

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
