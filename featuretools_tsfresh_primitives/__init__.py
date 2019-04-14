# flake8: noqa
from .abs_energy import AbsEnergy
from .absolute_sum_of_changes import AbsoluteSumOfChanges
from .agg_autocorrelation import AggAutocorrelation
from .approximate_entropy import ApproximateEntropy
from .agg_linear_trend import AggLinearTrend
from .ar_coefficient import ArCoefficient
from .augmented_dickey_fuller import AugmentedDickeyFuller
from .autocorrelation import Autocorrelation
from .binned_entropy import BinnedEntropy
from .c3 import C3
from .cid_ce import CidCe
from .change_quantiles import ChangeQuantiles
from .count_above_mean import CountAboveMean
from .count_below_mean import CountBelowMean
from .cwt_coefficients import CwtCoefficients
from .energy_ratio_by_chunks import EnergyRatioByChunks
from .fft_aggregated import FftAggregated
from .fft_coefficient import FftCoefficient
from .first_location_of_maximum import FirstLocationOfMaximum
from .first_location_of_minimum import FirstLocationOfMinimum
from .friedrich_coefficients import FriedrichCoefficients
from .has_duplicate import HasDuplicate
from .has_duplicate_max import HasDuplicateMax
from .has_duplicate_min import HasDuplicateMin
from .index_mass_quantile import IndexMassQuantile
from .kurtosis import Kurtosis
from .large_standard_deviation import LargeStandardDeviation
from .last_location_of_maximum import LastLocationOfMaximum
from .last_location_of_minimum import LastLocationOfMinimum
from .length import Length
from .linear_trend import LinearTrend
from .longest_strike_above_mean import LongestStrikeAboveMean
from .longest_strike_below_mean import LongestStrikeBelowMean
from .max_langevin_fixed_point import MaxLangevinFixedPoint
from .maximum import Maximum
from .mean import Mean
from .mean_abs_change import MeanAbsChange
from .mean_change import MeanChange
from .mean_second_derivative_central import MeanSecondDerivativeCentral
from .median import Median
from .minimum import Minimum
from .spkt_welch_density import SpktWelchDensity
from .symmetry_looking import SymmetryLooking

primitives = {
    'AbsEnergy': AbsEnergy,
    'AbsoluteSumOfChanges': AbsoluteSumOfChanges,
    'AggAutocorrelation': AggAutocorrelation,
    'AggLinearTrend': AggLinearTrend,
    'ApproximateEntropy': ApproximateEntropy,
    'ArCoefficient': ArCoefficient,
    'AugmentedDickeyFuller': AugmentedDickeyFuller,
    'Autocorrelation': Autocorrelation,
    'BinnedEntropy': BinnedEntropy,
    'C3': C3,
    'CidCe': CidCe,
    'ChangeQuantiles': ChangeQuantiles,
    'CountAboveMean': CountAboveMean,
    'CountBelowMean': CountBelowMean,
    'CwtCoefficients': CwtCoefficients,
    'EnergyRatioByChunks': EnergyRatioByChunks,
    'FftAggregated': FftAggregated,
    'FirstLocationOfMaximum': FirstLocationOfMaximum,
    'FirstLocationOfMinimum': FirstLocationOfMinimum,
    'FriedrichCoefficients': FriedrichCoefficients,
    'HasDuplicate': HasDuplicate,
    'HasDuplicateMax': HasDuplicateMax,
    'HasDuplicateMin': HasDuplicateMin,
    'IndexMassQuantile': IndexMassQuantile,
    'Kurtosis': Kurtosis,
    'LargeStandardDeviation': LargeStandardDeviation,
    'LastLocationOfMaximum': LastLocationOfMaximum,
    'LastLocationOfMinimum': LastLocationOfMinimum,
    'Length': Length,
    'LinearTrend': LinearTrend,
    'LongestStrikeAboveMean': LongestStrikeAboveMean,
    'LongestStrikeBelowMean': LongestStrikeBelowMean,
    'MaxLangevinFixedPoint': MaxLangevinFixedPoint,
    'Maximum': Maximum,
    'Mean': Mean,
    'MeanAbsChange': MeanAbsChange,
    'MeanChange': MeanChange,
    'MeanSecondDerivativeCentral': MeanSecondDerivativeCentral,
    'Median': Median,
    'Minimum': Minimum,
    'SpktWelchDensity': SpktWelchDensity,
    'SymmetryLooking': SymmetryLooking,
}
