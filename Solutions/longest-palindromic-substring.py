"""
Link: https://leetcode.com/problems/longest-palindromic-substring/
"""


def longestPalindrome(s):
    if len(s) == 1:
        return s
    longest_substring = s[0]
    start_index = 0
    end_index = 1
    while start_index < len(s):
        start_character = s[start_index]
        while end_index < len(s):
            end_character = s[end_index]
            # Check for possible palindrome
            if end_character == start_character:
                substring = s[start_index:end_index+1]
                if len(substring) > len(longest_substring):
                    checking = is_palindrome(substring)
                    if checking:
                        longest_substring = substring
            end_index += 1
        if len(longest_substring) > (len(s) / 2):
            return longest_substring
        start_index += 1
        end_index = start_index + 1
    return longest_substring


def is_palindrome(s):
    if len(s) == 1:
        return True
    if len(s) % 2 == 1:
        s = s[0:int(len(s) / 2)] + s[int(len(s) / 2) + 1:]
    first_half = s[0:int(len(s) / 2)]
    second_half = s[-1:int(len(s) / 2) - 1:-1]
    return first_half == second_half


def test_cases():
    list_of_cases = [
        {
            "s": "babad",
            "o": "bab"
        },
        {
            "s": "cbbd",
            "o": "bb"
        },
        {
            "s": "a",
            "o": "a"
        },
    ]
    for case in range(len(list_of_cases)):
        output = longestPalindrome(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(longestPalindrome("babad"))
test_cases()