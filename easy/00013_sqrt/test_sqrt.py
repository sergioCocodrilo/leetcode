import pytest
from sqrt import mySqrt

@pytest.mark.parametrize('x, expected', [
    (4, 2), 
    (8, 2),
    (2, 1),
])
def test_mySqrt(x: int, expected: int) -> None:
    assert mySqrt(x) == expected
