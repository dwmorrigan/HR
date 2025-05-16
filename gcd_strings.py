import math
from stopwatch import Stopwatch

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find a repeating pattern in both.
        # Mathy pattern. Not mine. Just testing fasty-ness
        if str1 + str2 != str2 + str1:
            return ""
        maxl = math.gcd(len(str1), len(str2))
        return str1[:maxl]

    def my_gcdOfStrings(self, str1: str, str2: str) -> str:
        # My patterns. Wordy and still roughly as fast as mathy solution.
        len1, len2 = len(str1), len(str2)
        if len1 == len2:
            short = min(str1, str2)
            long = max(str1, str2)
        elif len1 > len2:
            short = str2
            long = str1
        else:
            short = str1
            long = str2

        for i in range(len(short)):
            x = len(short)//len(short[i:])
            y = len(long)//len(short[i:])
            # MUCH faster
            if short[i:]*x==short and short[i:]*y==long:
                return short[i:]
            # MUCH slower
            # if short[i:]*short.count(short[i:]) == short and short[i:]*long.count(short[i:]) == long:
            #     return short[i:]
        return ""

x = Solution()
sw = Stopwatch()
sw.start()
print(x.gcdOfStrings("ABC", "ABCABC")) # ABC
print(x.gcdOfStrings("ABAB", "ABABAB")) # AB
print(x.gcdOfStrings("LEET", "CODE")) # 
print(x.gcdOfStrings("ACAC", "ACACAC")) # AC
print(x.gcdOfStrings("ABCABC", "ABC")) # ABC
print(x.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")) # TAUXX
print(x.gcdOfStrings("CXTXNCXTXNCXTXNCXTXNCXTXN", "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN")) # CXTXN
print(x.gcdOfStrings("AAAAAAAAA", "AAACCC")) # 
print(x.gcdOfStrings("NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM", "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM")) # "NLZGM"
print(x.gcdOfStrings("ABABCCABAB", "ABAB")) # 
sw.stop()
print(sw)
sw.restart()
print(x.my_gcdOfStrings("ABC", "ABCABC")) # ABC
print(x.my_gcdOfStrings("ABAB", "ABABAB")) # AB
print(x.my_gcdOfStrings("LEET", "CODE")) # 
print(x.my_gcdOfStrings("ACAC", "ACACAC")) # AC
print(x.my_gcdOfStrings("ABCABC", "ABC")) # ABC
print(x.my_gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")) # TAUXX
print(x.my_gcdOfStrings("CXTXNCXTXNCXTXNCXTXNCXTXN", "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN")) # CXTXN
print(x.my_gcdOfStrings("AAAAAAAAA", "AAACCC")) # 
print(x.my_gcdOfStrings("NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM", "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM")) # "NLZGM"
print(x.my_gcdOfStrings("ABABCCABAB", "ABAB")) # 
sw.stop()
print(sw)