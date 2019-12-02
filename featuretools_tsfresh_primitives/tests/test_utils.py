import pytest

from featuretools_tsfresh_primitives.utils import _pascal_case


@pytest.mark.parametrize('x,expected',
                         [('ab_ab_ab', 'AbAbAb'), ('c3', 'C3'), ('c_3', 'C3')])
def test_pascal_case(x, expected):
    assert _pascal_case(x) == expected
