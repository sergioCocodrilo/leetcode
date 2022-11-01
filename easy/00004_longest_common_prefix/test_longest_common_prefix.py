import pytest
from typing import List
from longest_common_prefix import longestCommonPrefix

@pytest.mark.parametrize('strs, expected', [
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], ''),
])
def test_longestCommonPrefix(strs: List[str], expected: str) -> None:
    assert longestCommonPrefix(strs) == expected
