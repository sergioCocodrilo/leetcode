import pytest
from valid_parentheses import isValid

@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("[", False),
])
def test_isValid(s: str, expected: bool) -> None:
    assert isValid(s) is expected
