# LC 334: Increasing Triplet Subsequence
# 7 July 2025 - 15ms execution time (67.95%) and 37.44mb memory (64.44%)

from stopwatch import Stopwatch


class Solution:
    # First attempt - works correctly for what the stated objective is, but not 
    # for what the tests are testing for.
    def increasingTriplet(self, nums):
        seq = 0
        last = nums[1]
        for i in range(len(nums)):
            if nums[i] <= last:
                last = nums[i]
                seq = 0
            else:
                seq +=1
                if seq == 2:
                    return True
                last = nums[i]
        return False
    
    # Second attempt - It took an embarassingly long time to realize working 
    # the problem from the end worked and was easy to visualize/understand.
    # If the number we are checking is >= the biggest number, that is now the 
    # biggest number. If it isn't, then check to see if it is >= to the middle 
    # number - if it is, then it is the new middle number. If the number being 
    # checked is less than the high number and less than the middle number, 
    # that is the sequence we are looking for.
    def it(self, nums):
            H, M = float('-inf'), float('-inf')
            for i in range(len(nums)-1, -1, -1):
                if nums[i] >= H:
                    H = nums[i]
                elif nums[i] >= M:
                    M = nums[i]
                else:
                    return True
            return False
    
    def itt(self, nums):
        # More pythonic. More faster. 7ms (99.69%)
        # Booyah.
        h, m = float('-inf'), float('-inf')
        for num in reversed(nums):
            if num >= h:
                h = num
            elif num >= m:
                m = num
            else:
                return True
        return False


def main():
    sw = Stopwatch()
    s = Solution()
    nums = [20,100,10,12,5,13]
    sw.start()
    s.it(nums)
    print(sw, 1)
    sw.restart()
    s.itt(nums)
    print(sw, 2)
    nums = [2, 4, -2, -3]
    sw.restart()
    s.it(nums)
    print(sw, 1)
    sw.restart()
    s.itt(nums)
    print(sw, 2)
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    sw.restart()
    s.it(nums)
    print(sw, 1)
    sw.restart()
    s.itt(nums)
    print(sw, 2)


if __name__ == "__main__":
    main()
