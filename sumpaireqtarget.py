from stopwatch import Stopwatch
sw = Stopwatch()

# Find first set of numbers in list that sum to target, return the position of the pair.
# Multiple iterations of this concept, looking to discover better methods


# for x in range(this_big): # block size
#     for i in nums:
#         print(x, i)
sw.restart()
#nums = [2, 11, 7, 15]
nums = [3,2,4]
#nums = [3, 3]
#target = 9
target = 6
#target = 6
for x in range(len(nums)):
    for y in range(x+1, len(nums)):
        A = nums[x]
        B = nums[y]
        if A+B==target:
            print([x, y], end='\t\t')
sw.stop()
print(sw)

def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            A = nums[x]
            B = nums[y]
            if A+B==target:
                return [x, y]

sw.restart()
print(twoSum(nums, target), end='\t\t')
sw.stop()
print(sw)

def xx(nums, target):
    dict_ = {}
    for i in range(len(nums)):
        dict_[nums[i]] = i
    for k, v in dict_.items():
        anti_target = target - k
        if (anti_target in dict_) and (dict_[anti_target] != v):
            return (v, dict_[anti_target])
            
sw.restart()
print(xx(nums, target), end='\t\t')
sw.stop()
print(sw)