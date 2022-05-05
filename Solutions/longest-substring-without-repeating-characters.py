"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)
    start = 0
    end = 1
    longest_count = 1
    mapper = {}
    while start < len(s):
        mapper[s[start]] = 0
        while end < len(s):
            if mapper.get(s[end]) is not None:
                break
            mapper[s[end]] = 0
            end += 1
        keys_count = len(mapper.keys())
        if keys_count > longest_count:
            longest_count = keys_count
        mapper = {}
        start += 1
        end = start + 1
    return longest_count


def test_cases():
    list_of_cases = [
        {
            "s": "abcabcbb",
            "o": 3
        },
        {
            "s": "bbbbb",
            "o": 1
        },
        {
            "s": "pwwkew",
            "o": 3
        },
        {
            "s":"aab",
            "o":2
        },
        {
            "s":"dvdf",
            "o":3
        },
        {
            "s":"jbpnbwwd",
            "o":4
        }
    ]
    for case in range(len(list_of_cases)):
        output = lengthOfLongestSubstring(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(lengthOfLongestSubstring("pwwkew"))
test_cases()
