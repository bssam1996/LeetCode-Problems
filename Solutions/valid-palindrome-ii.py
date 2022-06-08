"""
Link: https://leetcode.com/problems/valid-palindrome-ii
"""


def validPalindrome(self, s: str) -> bool:
    def isPalindrome(x):
        reversed_string = x[::-1]
        if x == reversed_string:
            return True
        for i in range(len(x)):
            if x[i] != reversed_string[i]:
                remove_one = x[0:i] + x[i + 1:]
                remove_two = reversed_string[0:i] + reversed_string[i + 1:]
                return remove_one == remove_one[::-1] or remove_two == remove_two[::-1]
        return False

    if len(s) == 1:
        return True
    return isPalindrome(s)