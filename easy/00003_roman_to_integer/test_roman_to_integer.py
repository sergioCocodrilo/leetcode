
import pytest
from roman_to_integer import romanToInt
from roman_to_integer import romanToInt2

@pytest.mark.parametrize('s, expected', [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_romanToInt(s: str, expected: int) -> None:
    assert romanToInt(s) == expected
    assert romanToInt2(s) == expected
