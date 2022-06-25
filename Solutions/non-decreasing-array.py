"""
Link: https://leetcode.com/problems/non-decreasing-array
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0
        for element in range(len(nums) - 1):
            if nums[element] > nums[element+1]:
                counter += 1
                if element == 0:
                    nums[element] = nums[element+1]
                else:
                    if nums[element + 1] < nums[element - 1]:
                        nums[element + 1] = nums[element]
                    else:
                        nums[element] = nums[element + 1]
                nums[element] = nums[element+1]
            if counter > 1:
                return False
        if counter == 0:
            return True
        for element in range(len(nums) - 1):
            if nums[element] > nums[element+1]:
                counter += 1
            if counter > 1:
                return False
        return True