"""
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""


def smallerNumbersThanCurrent(nums):
    nums_dict = {}
    for key in nums:
        nums_dict[key] = nums_dict.get(key,0) + 1
    sorted_keys = sorted(nums_dict.keys(),reverse=True)
    # print(sorted_keys)
    for key in range(len(sorted_keys)-1):
        nums_dict[sorted_keys[key]] = sum([nums_dict[hashed] for hashed in sorted_keys[key+1:]])
    nums_dict[sorted_keys[-1]] = 0
    nums = [nums_dict[num] for num in nums]
    return nums
    # print(nums_dict)

print(smallerNumbersThanCurrent([7,7,7,7]))
