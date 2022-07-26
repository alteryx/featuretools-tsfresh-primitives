from featuretools_tsfresh_primitives.primitives.abs_energy import AbsEnergy
from featuretools_tsfresh_primitives.primitives.absolute_sum_of_changes import (
    AbsoluteSumOfChanges,
)
from featuretools_tsfresh_primitives.primitives.agg_autocorrelation import (
    AggAutocorrelation,
)
from featuretools_tsfresh_primitives.primitives.agg_linear_trend import AggLinearTrend
from featuretools_tsfresh_primitives.primitives.approximate_entropy import (
    ApproximateEntropy,
)
from featuretools_tsfresh_primitives.primitives.ar_coefficient import ArCoefficient
from featuretools_tsfresh_primitives.primitives.augmented_dickey_fuller import (
    AugmentedDickeyFuller,
)
from featuretools_tsfresh_primitives.primitives.autocorrelation import Autocorrelation
from featuretools_tsfresh_primitives.primitives.binned_entropy import BinnedEntropy
from featuretools_tsfresh_primitives.primitives.c3 import C3
from featuretools_tsfresh_primitives.primitives.change_quantiles import ChangeQuantiles
from featuretools_tsfresh_primitives.primitives.cid_ce import CidCe
from featuretools_tsfresh_primitives.primitives.count_above import CountAbove
from featuretools_tsfresh_primitives.primitives.count_above_mean import CountAboveMean
from featuretools_tsfresh_primitives.primitives.count_below import CountBelow
from featuretools_tsfresh_primitives.primitives.count_below_mean import CountBelowMean
from featuretools_tsfresh_primitives.primitives.cwt_coefficients import CwtCoefficients
from featuretools_tsfresh_primitives.primitives.energy_ratio_by_chunks import (
    EnergyRatioByChunks,
)
from featuretools_tsfresh_primitives.primitives.fft_aggregated import (
    FftAggregated,
    ShortTermFftAggregated,
)
from featuretools_tsfresh_primitives.primitives.fft_coefficient import (
    FftCoefficient,
    ShortTermFftCoefficient,
)
from featuretools_tsfresh_primitives.primitives.first_location_of_maximum import (
    FirstLocationOfMaximum,
)
from featuretools_tsfresh_primitives.primitives.first_location_of_minimum import (
    FirstLocationOfMinimum,
)
from featuretools_tsfresh_primitives.primitives.friedrich_coefficients import (
    FriedrichCoefficients,
)
from featuretools_tsfresh_primitives.primitives.has_duplicate import HasDuplicate
from featuretools_tsfresh_primitives.primitives.has_duplicate_max import HasDuplicateMax
from featuretools_tsfresh_primitives.primitives.has_duplicate_min import HasDuplicateMin
from featuretools_tsfresh_primitives.primitives.index_mass_quantile import (
    IndexMassQuantile,
)
from featuretools_tsfresh_primitives.primitives.kurtosis import Kurtosis
from featuretools_tsfresh_primitives.primitives.large_standard_deviation import (
    LargeStandardDeviation,
)
from featuretools_tsfresh_primitives.primitives.last_location_of_maximum import (
    LastLocationOfMaximum,
)
from featuretools_tsfresh_primitives.primitives.last_location_of_minimum import (
    LastLocationOfMinimum,
)
from featuretools_tsfresh_primitives.primitives.length import Length
from featuretools_tsfresh_primitives.primitives.linear_trend import LinearTrend
from featuretools_tsfresh_primitives.primitives.linear_trend_timewise import (
    LinearTrendTimewise,
)
from featuretools_tsfresh_primitives.primitives.longest_strike_above_mean import (
    LongestStrikeAboveMean,
)
from featuretools_tsfresh_primitives.primitives.longest_strike_below_mean import (
    LongestStrikeBelowMean,
)
from featuretools_tsfresh_primitives.primitives.max_langevin_fixed_point import (
    MaxLangevinFixedPoint,
)
from featuretools_tsfresh_primitives.primitives.maximum import Maximum
from featuretools_tsfresh_primitives.primitives.mean import Mean
from featuretools_tsfresh_primitives.primitives.mean_abs_change import MeanAbsChange
from featuretools_tsfresh_primitives.primitives.mean_change import MeanChange
from featuretools_tsfresh_primitives.primitives.mean_second_derivative_central import (
    MeanSecondDerivativeCentral,
)
from featuretools_tsfresh_primitives.primitives.median import Median
from featuretools_tsfresh_primitives.primitives.minimum import Minimum
from featuretools_tsfresh_primitives.primitives.number_crossing_m import NumberCrossingM
from featuretools_tsfresh_primitives.primitives.number_cwt_peaks import NumberCwtPeaks
from featuretools_tsfresh_primitives.primitives.number_peaks import NumberPeaks
from featuretools_tsfresh_primitives.primitives.partial_autocorrelation import (
    PartialAutocorrelation,
)
from featuretools_tsfresh_primitives.primitives.percentage_of_reoccurring_datapoints_to_all_datapoints import (
    PercentageOfReoccurringDatapointsToAllDatapoints,
)
from featuretools_tsfresh_primitives.primitives.percentage_of_reoccurring_values_to_all_values import (
    PercentageOfReoccurringValuesToAllValues,
)
from featuretools_tsfresh_primitives.primitives.quantile import Quantile
from featuretools_tsfresh_primitives.primitives.range_count import RangeCount
from featuretools_tsfresh_primitives.primitives.ratio_beyond_r_sigma import (
    RatioBeyondRSigma,
)
from featuretools_tsfresh_primitives.primitives.ratio_value_number_to_time_series_length import (
    RatioValueNumberToTimeSeriesLength,
)
from featuretools_tsfresh_primitives.primitives.sample_entropy import SampleEntropy
from featuretools_tsfresh_primitives.primitives.skewness import Skewness
from featuretools_tsfresh_primitives.primitives.spkt_welch_density import (
    SpktWelchDensity,
)
from featuretools_tsfresh_primitives.primitives.standard_deviation import (
    StandardDeviation,
)
from featuretools_tsfresh_primitives.primitives.sum_of_reoccurring_data_points import (
    SumOfReoccurringDataPoints,
)
from featuretools_tsfresh_primitives.primitives.sum_of_reoccurring_values import (
    SumOfReoccurringValues,
)
from featuretools_tsfresh_primitives.primitives.sum_values import SumValues
from featuretools_tsfresh_primitives.primitives.symmetry_looking import SymmetryLooking
from featuretools_tsfresh_primitives.primitives.time_reversal_asymmetry_statistic import (
    TimeReversalAsymmetryStatistic,
)
from featuretools_tsfresh_primitives.primitives.value_count import ValueCount
from featuretools_tsfresh_primitives.primitives.variance import Variance
from featuretools_tsfresh_primitives.primitives.variance_larger_than_standard_deviation import (
    VarianceLargerThanStandardDeviation,
)

TSF_AGG_PRIMITIVES = [
    value
    for value in locals().values()
    if isinstance(value, type)
    and value not in [ShortTermFftAggregated, ShortTermFftCoefficient]
]
