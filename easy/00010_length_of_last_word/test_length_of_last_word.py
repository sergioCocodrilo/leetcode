import pytest
from length_of_last_word import lengthOfLastWord

@pytest.mark.parametrize('s, expected', [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
])
def test_lenghtOfLastWord(s:str, expected: int):
    assert lengthOfLastWord(s) == expected
