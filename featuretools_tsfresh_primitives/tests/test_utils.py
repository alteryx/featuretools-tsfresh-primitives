import pytest

from featuretools_tsfresh_primitives import (C3, CwtCoefficients, Minimum,
                                             Quantile)
from featuretools_tsfresh_primitives.utils import (_pascal_case,
                                                   primitives_from_fc_settings)


@pytest.mark.parametrize('x,expected',
                         [('ab_ab_ab', 'AbAbAb'), ('c3', 'C3'), ('c_3', 'C3')])
def test_pascal_case(x, expected):
    assert _pascal_case(x) == expected


def test_primitives_from_fc_settings():
    fc_settings = {'minimum': None,
                   'quantile': {'q': 0.1},
                   'C3': [{'lag': 1}, {'lag': 2}],
                   'cwt_coefficients': [{'widths': (2, 5), 'coeff': 1, 'w': 2},
                                        {'widths': (2, 5), 'coeff': 0, 'w': 5}]}

    actual = primitives_from_fc_settings(fc_settings)
    expected = [Minimum(),
                Quantile(q=0.1),
                C3(lag=1),
                C3(lag=2),
                CwtCoefficients(widths=[2, 5], coeff=1, w=2),
                CwtCoefficients(widths=[2, 5], coeff=0, w=5)]

    actual = [(primitive.__class__, primitive.get_args_string()) for primitive in actual]
    expected = [(primitive.__class__, primitive.get_args_string()) for primitive in expected]

    assert actual == expected
