
import pytest
from palindrome_number import isPalindrome

@pytest.mark.parametrize('x, expected', [
    (121, True),
    (-121, False),
    (10, False),
])
def test_isPalindrome(x: int, expected: bool) -> None:
    assert isPalindrome(x) == expected
