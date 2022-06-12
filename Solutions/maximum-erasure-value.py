"""
Link: https://leetcode.com/problems/maximum-erasure-value/
"""


def maximumUniqueSubarray(nums):
    if len(nums) == 1:
        return nums[0]
    seen = set()  # track visited elements in the window
    res = i = tot = 0
    for j in range(len(nums)):
        x = nums[j]
        # adjust the left bound of sliding window until you get all unique elements
        while i < j and x in seen:
            seen.remove(nums[i])
            tot -= nums[i]
            i += 1
        tot += x
        seen.add(x)
        res = max(res, tot)
    return res

#17
# print(maximumUniqueSubarray([4,2,4,5,6]))
#8
# print(maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
#16911
# print(maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))

print(maximumUniqueSubarray([i for i in range(10001)]*10))