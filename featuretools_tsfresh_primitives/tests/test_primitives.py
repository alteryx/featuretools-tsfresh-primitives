import featuretools as ft
from numpy.testing import assert_almost_equal
from pytest import fixture, mark
from tsfresh.feature_extraction import extract_features

from featuretools_tsfresh_primitives import (SUPPORTED_PRIMITIVES,
                                             comprehensive_fc_parameters,
                                             primitives_from_fc_settings)

PARAMETERS = comprehensive_fc_parameters()


@fixture(scope='session')
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


@fixture(scope='session')
def df(entityset):
    df = entityset['transactions'].df
    df = df.filter(regex='session_id|transaction_time|amount')
    df = df.set_index('transaction_time').sort_index()
    return df


def parametrize():
    values = {'argvalues': [], 'ids': []}
    for primitive in SUPPORTED_PRIMITIVES:
        parameter_list = PARAMETERS[primitive.name] or [{}]
        primitive_settings = {primitive.name: parameter_list}
        primitives = primitives_from_fc_settings(primitive_settings)
        items = zip(parameter_list, primitives)

        for parameters, primitive in items:
            item = {primitive.name: [parameters]}, primitive
            values['argvalues'].append(item)

            name = primitive.name.upper()
            args = primitive.get_args_string()
            if args: name += '(%s)' % args.lstrip(' ,')
            values['ids'].append(name)

    return values


@mark.parametrize('parameters,primitive', **parametrize())
def test_primitive(entityset, df, parameters, primitive):
    expected = extract_features(
        timeseries_container=df,
        column_id='session_id',
        default_fc_parameters=parameters,
    )

    base = entityset['transactions']['amount']

    if primitive.name == 'linear_trend_timewise':
        base = [base, entityset['transactions']['transaction_time']]

    feature = ft.Feature(
        base=base,
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
