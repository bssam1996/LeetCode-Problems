"""
Link: https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_set = set()
        for num in nums:
            if num in number_set:
                number_set.remove(num)
            else:
                number_set.add(num)
        return number_set.pop()