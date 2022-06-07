"""
Link: https://leetcode.com/problems/reverse-words-in-a-string/
"""


def reverseWords(self, s: str) -> str:
    s = s.strip().split(" ")
    s = list(filter(lambda x: x != "", s))
    return " ".join(s[::-1])