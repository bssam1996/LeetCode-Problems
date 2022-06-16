"""
Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
"""


def removeOccurrences(self, s: str, part: str) -> str:
    while s.count(part) > 0:
        s = s.replace(part, "", 1)
    return s