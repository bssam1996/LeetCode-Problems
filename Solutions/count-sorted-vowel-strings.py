"""
Link: https://leetcode.com/problems/count-sorted-vowel-strings/
"""


def countVowelStrings(n):
    r = 4
    n += 4
    return getFactorial(n) / (getFactorial(r) * (getFactorial(n - r)))


def getFactorial(n):
    if n == 1:
        return 1
    return n * getFactorial(n-1)


def test_cases():
    list_of_cases = [
        {
            "s": 1,
            "o": 5
        },
        {
            "s": 2,
            "o": 15
        },
        {
            "s": 33,
            "o": 66045
        },
    ]
    for case in range(len(list_of_cases)):
        output = countVowelStrings(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(countVowelStrings(7))
test_cases()
