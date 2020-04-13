import featuretools as ft
import pandas as pd
import pytest
from numpy.testing import assert_almost_equal
from pytest import fixture
from tsfresh.feature_extraction import extract_features

import featuretools_tsfresh_primitives.primitives
from featuretools_tsfresh_primitives.utils import (  # noqa
    comprehensive_fc_parameters, primitives_from_fc_settings,
    supported_primitives)

PRIMITIVES = {
    'abs_energy':
    featuretools_tsfresh_primitives.primitives.abs_energy.AbsEnergy,
    'absolute_sum_of_changes':
    featuretools_tsfresh_primitives.primitives.absolute_sum_of_changes.AbsoluteSumOfChanges,
    'agg_autocorrelation':
    featuretools_tsfresh_primitives.primitives.agg_autocorrelation.AggAutocorrelation,
    'agg_linear_trend':
    featuretools_tsfresh_primitives.primitives.agg_linear_trend.AggLinearTrend,
    'approximate_entropy':
    featuretools_tsfresh_primitives.primitives.approximate_entropy.ApproximateEntropy,
    'ar_coefficient':
    featuretools_tsfresh_primitives.primitives.ar_coefficient.ArCoefficient,
    'augmented_dickey_fuller':
    featuretools_tsfresh_primitives.primitives.augmented_dickey_fuller.AugmentedDickeyFuller,
    'autocorrelation':
    featuretools_tsfresh_primitives.primitives.autocorrelation.Autocorrelation,
    'binned_entropy':
    featuretools_tsfresh_primitives.primitives.binned_entropy.BinnedEntropy,
    'c3':
    featuretools_tsfresh_primitives.primitives.c3.C3,
    'change_quantiles':
    featuretools_tsfresh_primitives.primitives.change_quantiles.ChangeQuantiles,
    'cid_ce':
    featuretools_tsfresh_primitives.primitives.cid_ce.CidCe,
    'count_above_mean':
    featuretools_tsfresh_primitives.primitives.count_above_mean.CountAboveMean,
    'count_below_mean':
    featuretools_tsfresh_primitives.primitives.count_below_mean.CountBelowMean,
    'cwt_coefficients':
    featuretools_tsfresh_primitives.primitives.cwt_coefficients.CwtCoefficients,
    'energy_ratio_by_chunks':
    featuretools_tsfresh_primitives.primitives.energy_ratio_by_chunks.EnergyRatioByChunks,
    'fft_aggregated':
    featuretools_tsfresh_primitives.primitives.fft_aggregated.FftAggregated,
    'fft_coefficient':
    featuretools_tsfresh_primitives.primitives.fft_coefficient.FftCoefficient,
    'first_location_of_maximum':
    featuretools_tsfresh_primitives.primitives.first_location_of_maximum.FirstLocationOfMaximum,
    'first_location_of_minimum':
    featuretools_tsfresh_primitives.primitives.first_location_of_minimum.FirstLocationOfMinimum,
    'friedrich_coefficients':
    featuretools_tsfresh_primitives.primitives.friedrich_coefficients.FriedrichCoefficients,
    'has_duplicate':
    featuretools_tsfresh_primitives.primitives.has_duplicate.HasDuplicate,
    'has_duplicate_max':
    featuretools_tsfresh_primitives.primitives.has_duplicate_max.HasDuplicateMax,
    'has_duplicate_min':
    featuretools_tsfresh_primitives.primitives.has_duplicate_min.HasDuplicateMin,
    'index_mass_quantile':
    featuretools_tsfresh_primitives.primitives.index_mass_quantile.IndexMassQuantile,
    'kurtosis':
    featuretools_tsfresh_primitives.primitives.kurtosis.Kurtosis,
    'large_standard_deviation':
    featuretools_tsfresh_primitives.primitives.large_standard_deviation.LargeStandardDeviation,
    'last_location_of_maximum':
    featuretools_tsfresh_primitives.primitives.last_location_of_maximum.LastLocationOfMaximum,
    'last_location_of_minimum':
    featuretools_tsfresh_primitives.primitives.last_location_of_minimum.LastLocationOfMinimum,
    'length':
    featuretools_tsfresh_primitives.primitives.length.Length,
    'linear_trend':
    featuretools_tsfresh_primitives.primitives.linear_trend.LinearTrend,
    'longest_strike_above_mean':
    featuretools_tsfresh_primitives.primitives.longest_strike_above_mean.LongestStrikeAboveMean,
    'longest_strike_below_mean':
    featuretools_tsfresh_primitives.primitives.longest_strike_below_mean.LongestStrikeBelowMean,
    'max_langevin_fixed_point':
    featuretools_tsfresh_primitives.primitives.max_langevin_fixed_point.MaxLangevinFixedPoint,
    'maximum':
    featuretools_tsfresh_primitives.primitives.maximum.Maximum,
    'mean':
    featuretools_tsfresh_primitives.primitives.mean.Mean,
    'mean_abs_change':
    featuretools_tsfresh_primitives.primitives.mean_abs_change.MeanAbsChange,
    'mean_change':
    featuretools_tsfresh_primitives.primitives.mean_change.MeanChange,
    'mean_second_derivative_central':
    featuretools_tsfresh_primitives.primitives.mean_second_derivative_central.MeanSecondDerivativeCentral,
    'median':
    featuretools_tsfresh_primitives.primitives.median.Median,
    'minimum':
    featuretools_tsfresh_primitives.primitives.minimum.Minimum,
    'number_crossing_m':
    featuretools_tsfresh_primitives.primitives.number_crossing_m.NumberCrossingM,
    'number_cwt_peaks':
    featuretools_tsfresh_primitives.primitives.number_cwt_peaks.NumberCwtPeaks,
    'number_peaks':
    featuretools_tsfresh_primitives.primitives.number_peaks.NumberPeaks,
    'partial_autocorrelation':
    featuretools_tsfresh_primitives.primitives.partial_autocorrelation.PartialAutocorrelation,
    'percentage_of_reoccurring_datapoints_to_all_datapoints':
    featuretools_tsfresh_primitives.primitives.percentage_of_reoccurring_datapoints_to_all_datapoints.
    PercentageOfReoccurringDatapointsToAllDatapoints,
    'percentage_of_reoccurring_values_to_all_values':
    featuretools_tsfresh_primitives.primitives.percentage_of_reoccurring_values_to_all_values.
    PercentageOfReoccurringValuesToAllValues,
    'quantile':
    featuretools_tsfresh_primitives.primitives.quantile.Quantile,
    'range_count':
    featuretools_tsfresh_primitives.primitives.range_count.RangeCount,
    'ratio_beyond_r_sigma':
    featuretools_tsfresh_primitives.primitives.ratio_beyond_r_sigma.RatioBeyondRSigma,
    'ratio_value_number_to_time_series_length':
    featuretools_tsfresh_primitives.primitives.ratio_value_number_to_time_series_length.RatioValueNumberToTimeSeriesLength,
    'sample_entropy':
    featuretools_tsfresh_primitives.primitives.sample_entropy.SampleEntropy,
    'skewness':
    featuretools_tsfresh_primitives.primitives.skewness.Skewness,
    'spkt_welch_density':
    featuretools_tsfresh_primitives.primitives.spkt_welch_density.SpktWelchDensity,
    'standard_deviation':
    featuretools_tsfresh_primitives.primitives.standard_deviation.StandardDeviation,
    'sum_of_reoccurring_data_points':
    featuretools_tsfresh_primitives.primitives.sum_of_reoccurring_data_points.SumOfReoccurringDataPoints,
    'sum_of_reoccurring_values':
    featuretools_tsfresh_primitives.primitives.sum_of_reoccurring_values.SumOfReoccurringValues,
    'sum_values':
    featuretools_tsfresh_primitives.primitives.sum_values.SumValues,
    'symmetry_looking':
    featuretools_tsfresh_primitives.primitives.symmetry_looking.SymmetryLooking,
    'time_reversal_asymmetry_statistic':
    featuretools_tsfresh_primitives.primitives.time_reversal_asymmetry_statistic.TimeReversalAsymmetryStatistic,
    'value_count':
    featuretools_tsfresh_primitives.primitives.value_count.ValueCount,
    'variance':
    featuretools_tsfresh_primitives.primitives.variance.Variance,
    'variance_larger_than_standard_deviation':
    featuretools_tsfresh_primitives.primitives.variance_larger_than_standard_deviation.VarianceLargerThanStandardDeviation
}
PARAMETERS = comprehensive_fc_parameters()


@fixture(scope='session')
def entityset():
    return ft.demo.load_mock_customer(return_entityset=True)


@fixture(scope='session')
def df(entityset):
    df = pd.merge(entityset['sessions'].df, entityset['transactions'].df, on='session_id')
    return df[['session_id', 'transaction_time', 'amount']]


# def parametrize():
#     values = {'argvalues': [], 'ids': []}

#     for primitive in PRIMITIVES:
#         parameter_list = PARAMETERS[primitive.name] or [{}]
#         primitive_settings = {primitive.name: parameter_list}
#         primitives = primitives_from_fc_settings(primitive_settings)
#         items = zip(parameter_list, primitives)

#         for parameters, primitive in items:
#             item = {primitive.name: [parameters]}, primitive
#             values['argvalues'].append(item)

#             name = primitive.name.upper()
#             args = primitive.get_args_string()
#             if args: name += '(%s)' % args.lstrip(' ,')
#             values['ids'].append(name)


#     return values
def _comprehensive_fc_prims():
    """Yield a tuple (fc_setting, primitive, id)"""
    supported = {primitive.name for primitive in PRIMITIVES.values()}
    parameters = {key: value for key, value in PARAMETERS.items() if key in supported}

    # lag 0 on its own doesn't make sense
    parameters['partial_autocorrelation'] = [x for x in parameters['partial_autocorrelation'] if x['lag'] != 0]

    for fc_name, params_list in parameters.items():
        primitives = featuretools_tsfresh_primitives.primitives_from_fc_settings({fc_name: params_list})
        if not isinstance(params_list, list):
            params_list = [params_list]
        for params, primitive in zip(params_list, primitives):
            fc_setting = {fc_name: [params] if params else None}
            yield (fc_setting, primitive, str(fc_setting))


# @pytest.mark.parametrize('parameters,primitive', **parametrize())
@pytest.mark.parametrize(
    'parameters,primitive',
    [(x[0], x[1]) for x in _comprehensive_fc_prims()],
    ids=[x[2] for x in _comprehensive_fc_prims()],
)
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
