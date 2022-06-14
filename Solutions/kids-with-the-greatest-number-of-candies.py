"""
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""


def kidsWithCandies(candies, extraCandies):
    maximum_number = max(candies)
    result = []
    for candy in candies:
        if candy + extraCandies >= maximum_number:
            result.append(True)
        else:
            result.append(False)
    return result