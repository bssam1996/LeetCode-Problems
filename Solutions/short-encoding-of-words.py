"""
Link: https://leetcode.com/problems/short-encoding-of-words
"""

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        encoded_string = ""
        for word in words:
            if word + "#" in encoded_string:
                continue
            encoded_string += word + "#"
        return len(encoded_string)