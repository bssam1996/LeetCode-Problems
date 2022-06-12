"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


def minCostClimbingStairs(cost):
    n = len(cost)
    res = [0] * (n + 1)
    for i in range(2, n + 1):
        res[i] = min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2])
    return res[-1]

# print(minCostClimbingStairs([10,15,20]))
# print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1,1,1]))
# print(minCostClimbingStairs([1,0,0,1]))
print(minCostClimbingStairs([0,1,2,2]))
