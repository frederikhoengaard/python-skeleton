import pytest
from misc.example import square


@pytest.mark.parametrize("n, n_squared", [(2, 4), (3, 9), (4, 16), (5, 25)])
def test_square_passes(n, n_squared):
    assert square(n) == n_squared
