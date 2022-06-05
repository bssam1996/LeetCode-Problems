"""
Link: https://leetcode.com/problems/add-binary/
"""


def addBinary(a, b):
    sum_both = 0
    for char in range(len(a)):
        sum_both += 2**char * int(a[-1-char])
    for char in range(len(b)):
        sum_both += 2**char * int(b[-1-char])
    return format(sum_both,'b')
