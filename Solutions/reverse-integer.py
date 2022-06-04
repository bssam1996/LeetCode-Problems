"""
Link: https://leetcode.com/problems/reverse-integer/
"""


def reverse(x):
    negative_value = x < 0
    string_x = str(abs(x))
    output_number = int(string_x[::-1])
    if negative_value:
        output_number = -output_number
    if output_number > 2**31 - 1 or output_number < -2**31:
        return 0
    return output_number


def test_cases():
    list_of_cases = [
        {
            "s": 123,
            "o": 321
        },
        {
            "s": -123,
            "o": -321
        },
        {
            "s": 120,
            "o": 21
        },
        {
            "s":1563847412,
            "o":0
        }

    ]
    for case in range(len(list_of_cases)):
        output = reverse(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()

# print(numberOfBoomerangs(nums))
