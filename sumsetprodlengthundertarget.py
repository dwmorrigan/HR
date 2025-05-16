# How many sets can be made from list that sum'd by length are less than target

from stopwatch import Stopwatch
sw = Stopwatch()

sw.start()

# suba2 = len([nums[i:j] for i in range(len(nums)+1) for j in range(len(nums)+1) if nums[i:j] and sum(nums[i:j])*len(nums[i:j])<k])
# print(suba2)

nums = [5, 4, 3, 2, 1]
k = 10
this_big = len(nums)+1
suba2 = sum([1 if (nums[i:j] and sum(nums[i:j])*len(nums[i:j])<k) else 0 for i in range(this_big) for j in range(this_big)])
print(suba2)

sw.stop()
print(sw)