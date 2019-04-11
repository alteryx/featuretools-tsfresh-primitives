# flake8: noqa
from .abs_energy import AbsEnergy
from .absolute_sum_of_changes import AbsoluteSumOfChanges
from .agg_autocorrelation import AggAutocorrelation
from .approximate_entropy import ApproximateEntropy
from .ar_coefficient import ArCoefficient
from .agg_linear_trend import AggLinearTrend
from .energy_ratio_by_chunks import EnergyRatioByChunks
from .spkt_welch_density import SpktWelchDensity
from .symmetry_looking import SymmetryLooking

primitives = {
    'AbsEnergy': AbsEnergy,
    'AbsoluteSumOfChanges': AbsoluteSumOfChanges,
    'AggAutocorrelation': AggAutocorrelation,
    'AggLinearTrend': AggLinearTrend,
    'ApproximateEntropy': ApproximateEntropy,
    'ArCoefficient': ArCoefficient,
    'EnergyRatioByChunks': EnergyRatioByChunks,
    'SpktWelchDensity': SpktWelchDensity,
    'SymmetryLooking': SymmetryLooking,
}
