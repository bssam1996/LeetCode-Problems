"""
Link: https://leetcode.com/problems/largest-number/
"""


def largestNumber(nums):
    if len(nums) == 1:
        return str(nums[0])
    dict_nums = {
        "1":{
            "numbers":[]
        },
        "2":{
            "numbers":[]
        },
        "3":{
            "numbers":[]
        },
        "4":{
            "numbers":[]
        },
        "5":{
            "numbers":[]
        },
        "6":{
            "numbers":[]
        },
        "7":{
            "numbers":[]
        },
        "8":{
            "numbers":[]
        },
        "9":{
            "numbers":[]
        },
    }
    max_length = 0
    for number in nums:
        dict_nums[str(number)[0]]["numbers"].append(str(number))
        max_length = max(max_length, len(str(number))*2)
    result = ""
    for number in range(9, 0, -1):
        list_of_numbers = dict_nums[str(number)]["numbers"]
        if len(list_of_numbers) == 0:
            continue
        if len(list_of_numbers) == 1:
            result += str(list_of_numbers[0])
            continue
        # Sorting
        list_of_numbers.sort(key=lambda val: (str(val) * max_length)[:max_length], reverse=True)
        result += "".join([str(value) for value in list_of_numbers])
    return result

def test_cases():
    list_of_cases = [
        {
            "s": [10,2],
            "o": "210"
        },
        {
            "s": [3,30,34,5,9],
            "o": "9534330"
        },
        {
            "s": [337,373,3],
            "o": "3733373"
        },
        {
            "s": [432,43243],
            "o": "43243432"
        },
        {
            "s": [111311, 1113],
            "o": "1113111311"
        },


    ]
    for case in range(len(list_of_cases)):
        output = largestNumber(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)

test_cases()