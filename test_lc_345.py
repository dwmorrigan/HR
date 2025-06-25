import pytest
from lc_345 import Solution

@pytest.fixture(autouse=True)
def setup():
    pass # I don't want to forget this but I also don't have a use for it yet.

def test_reverseVowels():
    x = Solution()
    s = "IceCreAm"
    assert x.reverseVowels(s) == "AceCreIm"
    s = "abcdefg"
    assert x.reverseVowels(s) == "ebcdafg"
    s = "leetcode"
    assert x.reverseVowels(s) == "leotcede"