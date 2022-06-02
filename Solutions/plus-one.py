"""
Link: https://leetcode.com/problems/plus-one
"""


def plusOne(digits):
    return [int(element) for element in list(str(int("".join(str(digits)[1:-1].replace(" ", "").split(","))) + 1)[::])]