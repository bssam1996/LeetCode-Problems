"""
Link: https://leetcode.com/problems/implement-strstr/
"""


def strStr(haystack: str, needle: str):
    if needle == "":
        return 0
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


def test_cases():
    list_of_cases = [
        {
            "s": "hello",
            "t": "ll",
            "o": 2
        },
        {
            "s": "aaaaa",
            "t": "bba",
            "o": -1
        },

    ]
    for case in range(len(list_of_cases)):
        output = strStr(list_of_cases[case]["s"], list_of_cases[case]["t"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(searchInsert([1,3,5,6],7))
test_cases()