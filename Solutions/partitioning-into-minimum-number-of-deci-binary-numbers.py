"""
Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
"""


def minPartitions(n):
    minimum = 0
    for char in n:
        minimum = max(minimum,int(char))
    return minimum