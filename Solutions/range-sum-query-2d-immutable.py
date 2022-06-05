"""
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""


def __init__(self, matrix: List[List[int]]):
    self.matrix = matrix


def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    # Time limit Exceeded
    total_sum = 0
    while row1 <= row2:
        total_sum += sum(self.matrix[row1][col1:(col2 + 1)])
        row1 += 1
    return total_sum