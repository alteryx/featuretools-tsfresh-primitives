from pytest import fixture

import featuretools as ft


@fixture
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


@fixture
def primitives():
    module = __import__(__name__)
    primitives = {primitive: getattr(module, primitive) for primitive in module.__all__}
    return primitives


@fixture
def parameters():
    return {
        'AggAutocorrelation': {
            'f_agg': 'mean',
            'maxlag': 3,
        },
        'AggLinearTrend': {
            'attr': 'slope',
            'chunk_len': 4,
            'f_agg': 'mean',
        },
        'EnergyRatioByChunks': {
            'num_segments': 10,
            'segment_focus': 5,
        },
        'SpktWelchDensity': {
            'coeff': 5,
        },
        'SymmetryLooking': {
            'r': .5,
        }
    }


def test_all_primitives(entityset, primitives, parameters):
    is_agg_primitive = lambda name: issubclass(primitives[name], ft.primitives.AggregationPrimitive)
    construct_primitive = lambda name: primitives[name](**parameters.get(name, {}))
    agg_primitives = [construct_primitive(name) for name in primitives if is_agg_primitive(name)]
    feature_matrix, features = ft.dfs(entityset=entityset, target_entity='customers', agg_primitives=agg_primitives)
    assert not feature_matrix.empty
