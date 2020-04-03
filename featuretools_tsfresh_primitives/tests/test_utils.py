from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

from featuretools_tsfresh_primitives.utils import (comprehensive_primitives,
                                                   supported_primitives)


def test_comprehensive_primitives():
    fc_parameters = ComprehensiveFCParameters()
    agg_primitives = comprehensive_primitives()

    for primitive in supported_primitives():
        instances = agg_primitives[primitive.name]
        inputs = fc_parameters[primitive.name] or [{}]
        assert len(instances) == len(inputs)
        items = zip(instances, inputs)

        for instance, inputs in items:
            assert instance.name == primitive.name

            for attribute, value in inputs.items():
                assert hasattr(instance, attribute)
                assert getattr(instance, attribute) == value
