"""
Link: https://leetcode.com/problems/maximum-subarray/
"""


def maxSubArray(nums):
    maxSum = float('-inf')
    currSum = 0

    for num in nums:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum

#6
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))