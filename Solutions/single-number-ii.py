"""
Link: https://leetcode.com/problems/single-number-ii/
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_of_repetition = 3
        return ((number_of_repetition * sum(set(nums))) - sum(nums)) // (number_of_repetition - 1)