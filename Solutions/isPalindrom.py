"""
Link: https://leetcode.com/problems/palindrome-number
"""


def isPalindrome(x):
    if x < 0:
        return False
    number_string = str(x)
    if len(number_string) == 1:
        return True
    if len(number_string) % 2 == 1:
        number_string = number_string[0:int(len(number_string) / 2)] + number_string[int(len(number_string) / 2) + 1:]
    first_half = number_string[0:int(len(number_string) / 2)]
    second_half = number_string[-1:int(len(number_string) / 2) - 1:-1]
    return first_half == second_half