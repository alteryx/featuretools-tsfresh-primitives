import json
import os

from pytest import fixture

import featuretools as ft

from . import primitives


@fixture
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


@fixture
def parameters():
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'test_primitives.json')
    return json.load(open(file, 'r'))


def test_all_primitives(entityset, parameters):
    is_agg_primitive = lambda name: issubclass(primitives[name], ft.primitives.AggregationPrimitive)
    construct_primitive = lambda name: primitives[name](**parameters.get(name, {}))
    agg_primitives = [construct_primitive(name) for name in primitives if is_agg_primitive(name)]
    feature_matrix, features = ft.dfs(entityset=entityset, target_entity='customers', agg_primitives=agg_primitives)
    assert not feature_matrix.empty
