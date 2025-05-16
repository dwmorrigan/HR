from stopwatch import Stopwatch

'''
String s, made of lowercase letters, and integer k
Delete x char from string s until no more than k distinct char remain
What is the min x required?

1 <= s.length() <= 16
1 <= k <= 16
'''

class Solution:
    def minD(self, s: str, k: int) -> int:
        # v2.0 - More pythonic and (on avg) faster
        uni = set(s)
        if len(uni) <= k:
            return 0
        hold_it = [[s.count(i), i] for i in uni]
        hold_it.sort()
        v = [x[0] for i, x in enumerate(hold_it) if i < (len(uni)-k)]
        return sum(v)


    def minDeletion(self, s: str, k: int) -> int:
        unique = set(s)
        # If the number of distinct characters is already equal to or less than the goal, just send it back.
        if len(unique) <= k:
            return 0
        # Each distinct character is counted so we know which ones to chop off first
        hold_it = []
        for each_distinct in unique:
            hold_it.append([s.count(each_distinct), each_distinct])
        # Love Python 
        hold_it.sort()
        # How many characters have we cut (v) and how many distinct characters we've cut (d)
        v, d = 0, 0
        for x in hold_it:
            v += x[0]
            d += 1
            # As soon as we've chopped off enough distinct characters to meet our requirement (k), send back the number of characters cut (v)
            if d >= len(unique)-k:
                return v

def main():
    sw = Stopwatch(10)
    solution = Solution()
    # Base tests
    sw.start()
    s = "abc"
    k = 2
    print(solution.minDeletion(s, k))
    # assert solution.minDeletion(s, k) == 1
    s = "aabb"
    k = 2
    print(solution.minDeletion(s, k))
    # assert solution.minDeletion(s, k) == 0
    s = "yyyzz"
    k = 1
    print(solution.minDeletion(s, k))
    # assert solution.minDeletion(s, k) == 2
    s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddeeeeeeefffffffggggggghhhhhhhiiiiiiijjjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooopppppppqqqqqqqrrrrrrrssssssstttttttuuuuuuuvvvvvvvwxyz"
    k = 7
    print(solution.minDeletion(s, k))
    # assert solution.minDeletion(s, k) == 0
    sw.stop()
    print(sw)

    # v2.0 Tests
    sw.restart()
    s = "abc"
    k = 2
    print(solution.minD(s, k))
    s = "aabb"
    k = 2
    print(solution.minD(s, k))
    s = "yyyzz"
    k = 1
    print(solution.minD(s, k))
    s = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddeeeeeeefffffffggggggghhhhhhhiiiiiiijjjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooopppppppqqqqqqqrrrrrrrssssssstttttttuuuuuuuvvvvvvvwxyz"
    k = 7
    print(solution.minD(s, k))

    sw.stop()
    print(sw)



if __name__ == "__main__":
    main()
