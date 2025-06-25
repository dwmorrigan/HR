import pytest
from lc_345 import Solution

@pytest.fixture(autouse=True)
def solution():
    solution = Solution()
    return solution

def test_1(solution):
    s = "IceCreAm"
    assert solution.reverseVowels(s) == "AceCreIm"

def test_2(solution):
    s = "abcdefg"
    assert solution.reverseVowels(s) == "ebcdafg"

def test_3(solution):
    s = "leetcode"
    assert solution.reverseVowels(s) == "leotcede"