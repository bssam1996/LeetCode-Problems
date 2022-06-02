"""
Link: https://leetcode.com/problems/length-of-last-word/
"""


def lengthOfLastWord(s):
    return len(s.strip().split(" ")[-1])

