"""
Link: https://leetcode.com/problems/single-number-iii/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [i for i in counter if counter[i] == 1]