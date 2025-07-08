# Within O(n) time and using no division, return an int array 
# where answer[i] = product of all nums EXCEPT nums[i]

from stopwatch import Stopwatch

# First attempt
# Loops in loops - fails to meet within O(n) time

# Second attempt
def productExceptSelf(nums):
    left, right = [0]*len(nums), [0]*len(nums)
    left_mult, right_mult = 1, 1
    for i in range(len(nums)):
        j = -i - 1
        left[i] = left_mult
        right[j] = right_mult
        left_mult *= nums[i]
        right_mult *= nums[j]
    nums = [l*r for l, r in zip(left, right)]
    return nums

# Third attempt, aiming for improved execution time and reduced 
# memory usage. Not identifiably faster, but seems to use less memory.
def t(n):
    l, r = 1, 1
    size = len(n)
    comb = [1]*size #len(n)
    for i in range(size): #len(n)):
        comb[i] = l * comb[i]
        comb[-i-1] = r * comb[-i-1]
        l *= n[i]
        r *= n[-i-1]
    return comb
    

def main():
    n = [111, 222, 333, 444, 555, 666, 777, 888, 999, 101010, 111111, 121212, 131313, 141414, 151515, 161616, 171717, 181818, 191919, 987654321, 2340523495822398457290843750234, 234895720983475902374, 9283749, 28934758927, 234509283745, 234523452346, 2346254, 2345236363452345365346, 3452345, 345234, 234623626, 23452345, 2623462345243523423623452324523452435236, 23452345234523452345234523452, 23423462346253434574573453456456334534, 457373452346345, 236253457473454624624336245475347354753245426, 2342346246,2342345234523,234275547345,734573457,34573457373457347345,3457357345473547547537354,543334573454535434575475343,342456245]

    sw = Stopwatch()
    sw.start()
    productExceptSelf(n)
    sw.stop()
    print(sw)
    sw.restart()
    t(n)
    sw.stop()
    print(sw)


if __name__ == "__main__":
    main()
