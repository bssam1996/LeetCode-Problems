"""
Link: https://leetcode.com/problems/zigzag-conversion/
"""

""" P     I    N
    A   L S  I G
    Y A   H R
    P     I     """
# "PAYPALISHIRING"
# "PINALSIGYAHRPI"
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    char_array = [[] for i in range(numRows)]

    row = 0
    direction = -1

    for c in s:
        char_array[row].append(c)
        if row == 0 or row == numRows - 1:
            direction = direction * -1
        row = row + direction

    result = "".join("".join(element) for element in char_array)
    return result



print(convert("PAYPALISHIRING",4))