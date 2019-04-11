# flake8: noqa
from .abs_energy import AbsEnergy
from .agg_autocorrelation import AggAutocorrelation
from .agg_linear_trend import AggLinearTrend
from .energy_ratio_by_chunks import EnergyRatioByChunks
from .spkt_welch_density import SpktWelchDensity
from .symmetry_looking import SymmetryLooking

primitives = {
    'AbsEnergy': AbsEnergy,
    'AggAutocorrelation': AggAutocorrelation,
    'AggLinearTrend': AggLinearTrend,
    'EnergyRatioByChunks': EnergyRatioByChunks,
    'SpktWelchDensity': SpktWelchDensity,
    'SymmetryLooking': SymmetryLooking,
}
