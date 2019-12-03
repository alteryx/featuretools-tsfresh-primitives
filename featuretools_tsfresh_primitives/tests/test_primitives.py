import json
import os

import featuretools as ft
import numpy.testing
import pandas as pd
import pytest
from pytest import fixture
from tsfresh.feature_extraction import extract_features
from tsfresh.feature_extraction.settings import ComprehensiveFCParameters

import featuretools_tsfresh_primitives

PRIMITIVES = {
    "AbsEnergy": featuretools_tsfresh_primitives.AbsEnergy,
    "AbsoluteSumOfChanges": featuretools_tsfresh_primitives.AbsoluteSumOfChanges,
    "AggAutocorrelation": featuretools_tsfresh_primitives.AggAutocorrelation,
    "AggLinearTrend": featuretools_tsfresh_primitives.AggLinearTrend,
    "ApproximateEntropy": featuretools_tsfresh_primitives.ApproximateEntropy,
    "ArCoefficient": featuretools_tsfresh_primitives.ArCoefficient,
    "AugmentedDickeyFuller": featuretools_tsfresh_primitives.AugmentedDickeyFuller,
    "Autocorrelation": featuretools_tsfresh_primitives.Autocorrelation,
    "BinnedEntropy": featuretools_tsfresh_primitives.BinnedEntropy,
    "C3": featuretools_tsfresh_primitives.C3,
    "ChangeQuantiles": featuretools_tsfresh_primitives.ChangeQuantiles,
    "CidCe": featuretools_tsfresh_primitives.CidCe,
    "CountAboveMean": featuretools_tsfresh_primitives.CountAboveMean,
    "CountBelowMean": featuretools_tsfresh_primitives.CountBelowMean,
    "CwtCoefficients": featuretools_tsfresh_primitives.CwtCoefficients,
    "EnergyRatioByChunks": featuretools_tsfresh_primitives.EnergyRatioByChunks,
    "FftAggregated": featuretools_tsfresh_primitives.FftAggregated,
    "FftCoefficient": featuretools_tsfresh_primitives.FftCoefficient,
    "FirstLocationOfMaximum": featuretools_tsfresh_primitives.FirstLocationOfMaximum,
    "FirstLocationOfMinimum": featuretools_tsfresh_primitives.FirstLocationOfMinimum,
    "FriedrichCoefficients": featuretools_tsfresh_primitives.FriedrichCoefficients,
    "HasDuplicate": featuretools_tsfresh_primitives.HasDuplicate,
    "HasDuplicateMax": featuretools_tsfresh_primitives.HasDuplicateMax,
    "HasDuplicateMin": featuretools_tsfresh_primitives.HasDuplicateMin,
    "IndexMassQuantile": featuretools_tsfresh_primitives.IndexMassQuantile,
    "Kurtosis": featuretools_tsfresh_primitives.Kurtosis,
    "LargeStandardDeviation": featuretools_tsfresh_primitives.LargeStandardDeviation,
    "LastLocationOfMaximum": featuretools_tsfresh_primitives.LastLocationOfMaximum,
    "LastLocationOfMinimum": featuretools_tsfresh_primitives.LastLocationOfMinimum,
    "Length": featuretools_tsfresh_primitives.Length,
    "LinearTrend": featuretools_tsfresh_primitives.LinearTrend,
    "LongestStrikeAboveMean": featuretools_tsfresh_primitives.LongestStrikeAboveMean,
    "LongestStrikeBelowMean": featuretools_tsfresh_primitives.LongestStrikeBelowMean,
    "MaxLangevinFixedPoint": featuretools_tsfresh_primitives.MaxLangevinFixedPoint,
    "Maximum": featuretools_tsfresh_primitives.Maximum,
    "Mean": featuretools_tsfresh_primitives.Mean,
    "MeanAbsChange": featuretools_tsfresh_primitives.MeanAbsChange,
    "MeanChange": featuretools_tsfresh_primitives.MeanChange,
    "MeanSecondDerivativeCentral": featuretools_tsfresh_primitives.MeanSecondDerivativeCentral,
    "Median": featuretools_tsfresh_primitives.Median,
    "Minimum": featuretools_tsfresh_primitives.Minimum,
    "NumberCrossingM": featuretools_tsfresh_primitives.NumberCrossingM,
    "NumberCwtPeaks": featuretools_tsfresh_primitives.NumberCwtPeaks,
    "NumberPeaks": featuretools_tsfresh_primitives.NumberPeaks,
    "PartialAutocorrelation": featuretools_tsfresh_primitives.PartialAutocorrelation,
    "PercentageOfReoccurringDatapointsToAllDatapoints": featuretools_tsfresh_primitives.PercentageOfReoccurringDatapointsToAllDatapoints,
    "PercentageOfReoccurringValuesToAllValues": featuretools_tsfresh_primitives.PercentageOfReoccurringValuesToAllValues,
    "Quantile": featuretools_tsfresh_primitives.Quantile,
    "RangeCount": featuretools_tsfresh_primitives.RangeCount,
    "RatioBeyondRSigma": featuretools_tsfresh_primitives.RatioBeyondRSigma,
    "RatioValueNumberToTimeSeriesLength": featuretools_tsfresh_primitives.RatioValueNumberToTimeSeriesLength,
    "SampleEntropy": featuretools_tsfresh_primitives.SampleEntropy,
    "Skewness": featuretools_tsfresh_primitives.Skewness,
    "SpktWelchDensity": featuretools_tsfresh_primitives.SpktWelchDensity,
    "StandardDeviation": featuretools_tsfresh_primitives.StandardDeviation,
    "SumOfReoccurringDataPoints": featuretools_tsfresh_primitives.SumOfReoccurringDataPoints,
    "SumOfReoccurringValues": featuretools_tsfresh_primitives.SumOfReoccurringValues,
    "SumValues": featuretools_tsfresh_primitives.SumValues,
    "SymmetryLooking": featuretools_tsfresh_primitives.SymmetryLooking,
    "TimeReversalAsymmetryStatistic": featuretools_tsfresh_primitives.TimeReversalAsymmetryStatistic,
    "ValueCount": featuretools_tsfresh_primitives.ValueCount,
    "Variance": featuretools_tsfresh_primitives.Variance,
    "VarianceLargerThanStandardDeviation": featuretools_tsfresh_primitives.VarianceLargerThanStandardDeviation,
}


@fixture(scope='session')
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


@fixture
def parameters():
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'test_primitives.json')
    return json.load(open(file, 'r'))


def test_all_primitives(entityset, parameters):
    is_agg_primitive = lambda name: issubclass(PRIMITIVES[name], ft.primitives.AggregationPrimitive)
    construct_primitive = lambda name: PRIMITIVES[name](**parameters.get(name, {}))
    agg_primitives = [construct_primitive(name) for name in PRIMITIVES if is_agg_primitive(name)]
    assert len(agg_primitives) == len(PRIMITIVES)
    feature_matrix, features = ft.dfs(entityset=entityset, target_entity='sessions', agg_primitives=agg_primitives)
    assert not feature_matrix.empty
    used_primitives = set({})

    for feature in features:
        prims = {type(base_feat.primitive) for base_feat in feature.base_features}
        prims.add(type(feature.primitive))
        used_primitives = used_primitives | prims

    for primitive in PRIMITIVES.values():
        assert primitive in used_primitives


@fixture(scope='session')
def df(entityset):
    df = pd.merge(entityset['sessions'].df, entityset['transactions'].df, on='session_id')
    return df[['session_id', 'transaction_time', 'amount']]


def _comprehensive_fc_prims():
    """Yield a tuple (fc_setting, primitive, id)"""
    fc_params = ComprehensiveFCParameters()
    # linear_trend_timewise not supported by featuretools-tsfresh-primitives atm
    fc_params.pop('linear_trend_timewise')
    # lag 0 on its own doesn't make sense
    fc_params['partial_autocorrelation'] = [x for x in fc_params['partial_autocorrelation'] if
                                            x['lag'] != 0]

    for fc_name, params_list in fc_params.items():
        primitives = featuretools_tsfresh_primitives.primitives_from_fc_settings({fc_name: params_list})
        if not isinstance(params_list, list):
            params_list = [params_list]
        for params, primitive in zip(params_list, primitives):
            fc_setting = {fc_name: [params] if params else None}
            yield (fc_setting, primitive, str(fc_setting))


@pytest.mark.parametrize('fc_setting,primitive',
                         [(x[0], x[1]) for x in _comprehensive_fc_prims()],
                         ids=[x[2] for x in _comprehensive_fc_prims()])
def test_primitive(entityset, df, fc_setting, primitive):
    expected = extract_features(df,
                                column_id='session_id',
                                column_sort='transaction_time',
                                default_fc_parameters=fc_setting)
    actual, _ = ft.dfs(entityset=entityset,
                       max_depth=1,
                       target_entity='sessions',
                       trans_primitives=[],
                       where_primitives=[],
                       agg_primitives=[primitive])
    actual = actual.filter(regex='transactions.amount')

    numpy.testing.assert_almost_equal(expected.values, actual.values)
