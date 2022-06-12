"""
Link: https://leetcode.com/problems/longest-common-prefix/
"""


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    longest_prefix = ""
    minimum_length_string = min(strs, key=len)
    for char in range(len(minimum_length_string)):
        end = False
        for element in strs:
            if element[char] != minimum_length_string[char]:
                end = True
                break

        if not end:
            longest_prefix += minimum_length_string[char]
        else:
            break

    return longest_prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
