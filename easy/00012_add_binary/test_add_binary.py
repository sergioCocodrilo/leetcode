import pytest
from add_binary import addBinary

@pytest.mark.parametrize('a, b, expected', [
    ('11', '1', '100'),
    ('1010', '1011', '10101'),
])
def test_addBinary(a: str, b: str, expected: str) -> None:
    assert addBinary(a, b) == expected
