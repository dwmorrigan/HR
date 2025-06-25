# Can Place Flowers
# Input: flowerbed: List of 0s and 1s (representing flowerpots), none contiguous, <= 2*10**4
# Input: N (representing # of additional flowerpots to add) <= len(flowerbed)
# Ouput: 'true' or 'false': Can N flowerpots be added without creating contiguous flowerpots?

    # [] - empty: can fit 1
    # 1 - 0 zero - no fit
    # 0 - 1 zero - fit 1 (1,0),0,(0,1)
    # 1,0 or 0,1 - 1 zero - no fit
    #   1,0,1 - 1 zero - no fit
    #   1,0,0,1 - 2 zero - no fit
    #   1,0,0,0,1 - 3 zero - fit 1
    # 0 - 1 zero - fit 1 (1,0),0,(0,1)
    #   1,0,0,0,0,1 - 4 zero - fit 1
    # 0,0 - 2 zero - fit 1 (1,0),0,0,(0,1) fit 1
    # 0 - can fit 1 (1,0),0,(0,1)
    # 0,0 - 2 zero - fit 1 (1,0),0,0,(0,1)??
    #   1,0,0,0,0,0,1 - 5 zero - fit 2
    #   1,0,0,0,0,0,0,1 - 6 zero - fit 2
    # 0,0,0 - 3 zero - fit 2 (1,0),0,0,0,(0,1)??
    # 0,0,0,0 - 4 zero - fit 2 (1,0),0,0,0,0,(0,1)??
    #   1,0,0,0,0,0,0,0,1 - 7 zero - fit 3
    #   1,0,0,0,0,0,0,0,0,1 - 8 zero - fit 3
    # 0,0,0,0,0 - 5 zero - fit 3 - fit 3 (1,0),0,0,0,0,0,(0,1)
    # 0,0,1 - 2 starts - fit 1 maybe (1,0),0,0,1?? 

from itertools import product
from stopwatch import Stopwatch

class Solution:
    def canPlaceFlowers( self, flowerbed: list[ int ], n: int ) -> bool:
        def can_fit(s,n):
            if n <= s:
                return True
            return False

        # hos_long, hos_count, hos_zero, hos_one inspired by Jen McCabe
        s = flowerbed
        sum = 0
        hos_long = len(s)
        # I think the order of my if/then tests could be optimized
        if hos_long < 1: # If the flowerbed is empty, then 1 pot can be placed
            return can_fit(1, n)
        else: # If the begining or end is a 0, tacking on a 10 or 01 allows the same pattern to be used for all flowerbeds.
            if s[0] != 1:
                s = [1,0] + s
            if s[-1] != 1:
                s.append(0)
                s.append(1)
        hos_count = s.count(1)
        if hos_count == 2: # This situation occurs when the first and last digits are 1 - and no other locations are 1. Possibly not necessary
            hos_zero = s.count(0)
            sum = round((hos_zero-1.1)/2)
            return can_fit(sum, n)
        # 3+ pots: Find the first 1, find the second 1. Calc the potential pots. Find the next pot. Calc the potential pots. Repeat until done.
        hos_one = s.count(1) - 1
        a = s.index(1)
        for _ in range(hos_one):
            b = s.index(1, a+1)
            hos_zero = s[a:b].count(0)
            sum += round((hos_zero-1.1)/2)
            a = b
        return can_fit(sum, n)
        

def f(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        # Check if the current plot is empty.
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty.
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            # If both plots are empty, we can plant a flower here.
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n


def main():
    sw = Stopwatch()
    s = Solution( )
    n = 3
    # I want to test many possible combinations. To do so, I make all of the 
    # combinations of 0 and 1 that are of particular length. If that's a valid 
    # combination (no two 1s are adjacent), then calculate how many flowerpots 
    # can be added and if that is >= the number of pots we want to add (n).
    for beep in range( 17, 20 ):
        matrices = list( product( [ 0, 1 ], repeat=beep ) )
        for x in matrices:
            nope = False
            x = list( x )
            for xx in range(len(x)-1):
                if x[xx] == 1 and x[xx+1] == 1:
                    nope = True
                    break
            if not nope:
                sw.start
                a = s.canPlaceFlowers(x,n) # My solution
                sw.stop()
                print(sw, end=' ')
                sw.restart()
                b = f(x,n) # LeetCode's tutorial solution
                sw.stop()
                print(sw, end=' ')
                print(x, a, b)


if __name__ == "__main__":
    main()

