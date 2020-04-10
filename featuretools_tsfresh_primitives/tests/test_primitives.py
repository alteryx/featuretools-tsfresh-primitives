import featuretools as ft
import pytest
from numpy.testing import assert_almost_equal
from pytest import fixture
from tsfresh.feature_extraction import extract_features

from featuretools_tsfresh_primitives.utils import (comprehensive_fc_parameters,
                                                   primitives_from_fc_settings,
                                                   supported_primitives)


@fixture(scope='session')
def df():
    df = ft.demo.load_mock_customer(return_single_table=True)
    df = df.filter(regex='session_id|transaction_time|amount')
    return df


@fixture(scope='session')
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


def parametrize():
    values = {'argvalues': [], 'ids': []}
    fc_parameters = comprehensive_fc_parameters()

    for primitive in supported_primitives():
        parameter_list = fc_parameters[primitive.name] or [{}]
        primitive_settings = {primitive.name: parameter_list}
        primitives = primitives_from_fc_settings(primitive_settings)
        items = zip(parameter_list, primitives)

        for parameters, primitive in items:
            item = {primitive.name: [parameters]}, primitive
            values['argvalues'].append(item)

            name = primitive.name.upper()
            args = primitive.get_args_string()
            name += '(%s)' % args.lstrip(',')
            values['ids'].append(name)

    return values


@pytest.mark.parametrize('parameters,primitive', **parametrize())
def test_primitive(entityset, df, parameters, primitive):
    expected = extract_features(
        timeseries_container=df,
        column_id='session_id',
        column_sort='transaction_time',
        default_fc_parameters=parameters,
    )

    feature = ft.Feature(
        base=entityset['transactions']['amount'],
        parent_entity=entityset['sessions'],
        primitive=primitive,
    )

    actual = ft.calculate_feature_matrix(
        features=[feature],
        entityset=entityset,
    )

    assert_almost_equal(
        actual=actual.values,
        desired=expected.values,
    )
