# Testing for correctness of regex patterns in Python
# HackerRank's test input (as of 09-Jun-2025) returns correct for both sample 
# patterns when using Python3.11, which is the version I am using in this repo. 
# However, it fails the HackerRank tests which allow for PyPy2, PyPy3, or 
# Python 2. I have kept the code correct for Python3.11, despite it failing the 
# challenge.

# Sample input:
# 2
# .*\+
# .*+

# Expected output:
# True
# False

import re

def check(rgx):
    try:
        re.compile(rgx)
        return True
    except re.PatternError:
        return False
        
        
def main():
    T = int(input())
    for i in range(T):
        rgx = input()
        print(check(rgx))


if __name__ == "__main__":
    main()