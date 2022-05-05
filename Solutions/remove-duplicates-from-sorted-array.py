"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        counter = 1
        while counter < len(nums):
            if nums[counter] == nums[counter-1]:
                del nums[counter]
                counter -= 1
            counter += 1
        return len(nums)