from typing import List

'''
Given a list of how much candy each kid has, would that kid have the MOST candy if we gave them all of the extraCandies?
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = list()
        most_candies = max(candies)
        for x in range(len(candies)):
            if (candies[x] + extraCandies) >= most_candies:
                results.append(True)
            else:
                results.append(False)
        # This works, absoultely kills the list comprehension, and is so slow compared to my basic if/then logic 
        # return [True if candies[x]+extraCandies >= max(candies) else False for x in range(len(candies))]
        return results


def main():
    s = Solution()
    c = [2, 3, 5, 1, 3]
    e = 3
    print(s.kidsWithCandies(c, e))
    c = [4, 2, 1, 1, 2]
    e = 1
    print(s.kidsWithCandies(c, e))
    c = [12, 1, 12]
    e = 10
    print(s.kidsWithCandies(c, e))

if __name__ == "__main__":
    main()