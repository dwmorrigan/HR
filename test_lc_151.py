import pytest
from lc_151 import Solution

@pytest.fixture(autouse=True)
def solution():
    solution = Solution()
    return solution

def test_1(solution):
    s = "the sky is blue"
    assert solution.reverseWords(s) == "blue is sky the"

def test_2(solution):
    s = "  hello world  "
    assert solution.reverseWords(s) == "world hello"

def test_3(solution):
    s = "a good   example"
    assert solution.reverseWords(s) == "example good a"

def test_4(solution):
    s = "blue"
    assert solution.reverseWords(s) == "blue"
