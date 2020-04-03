import featuretools as ft
import pytest
from numpy.testing import assert_almost_equal
from pytest import fixture
from tsfresh.feature_extraction import extract_features
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

from featuretools_tsfresh_primitives import comprehensive_primitives

BLACKLIST = [
    # when a partial autocorrelation has a lag of zero,
    # an error is raised from `tsfresh.feature_extraction.extract_features`
    'PARTIAL_AUTOCORRELATION(transactions.amount, lag=0)'
]


@fixture(scope='session')
def df():
    df = ft.demo.load_mock_customer(return_single_table=True)
    df = df.filter(regex='session_id|transaction_time|amount')
    return df


@fixture(scope='session')
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


def parameterize():
    values = {'argvalues': [], 'ids': []}
    fc_parameters = ComprehensiveFCParameters()
    agg_primitives = comprehensive_primitives(fc_parameters)
    es = ft.demo.load_mock_customer(return_entityset=True)

    for key in agg_primitives:
        parameters = fc_parameters[key] or [{}]
        items = zip(parameters, agg_primitives[key])

        for parameters, primitive in items:
            feature = ft.Feature(
                base=es['transactions']['amount'],
                parent_entity=es['sessions'],
                primitive=primitive,
            )

            name = feature.generate_name()
            item = {key: [parameters]}, feature
            values['argvalues'].append(item)
            values['ids'].append(name)

    return values


@pytest.mark.parametrize('fc_parameters,feature', **parameterize())
def test_primitive(entityset, df, fc_parameters, feature):
    name = feature.generate_name()
    if name in BLACKLIST: return

    expected = extract_features(
        timeseries_container=df,
        column_id='session_id',
        column_sort='transaction_time',
        default_fc_parameters=fc_parameters,
    )

    actual = ft.calculate_feature_matrix(
        features=[feature],
        entityset=entityset,
    )

    assert_almost_equal(
        actual=actual.values,
        desired=expected.values,
    )
