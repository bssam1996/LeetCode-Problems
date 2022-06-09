"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


def two_sum(numbers, target):
    numbers_dict = {}
    for base_counter in range(len(numbers)):
        if numbers_dict.get(numbers[base_counter]) is None:
            numbers_dict[numbers[base_counter]] = {
                "counter": 1,
                "location": base_counter
            }
        else:
            numbers_dict[numbers[base_counter]]["counter"] += 1
            numbers_dict[numbers[base_counter]]["location"] = base_counter
    for base_counter in range(len(numbers)):
        second_number = target - numbers[base_counter]
        if numbers_dict.get(second_number) is None:
            continue
        if numbers_dict.get(second_number)["counter"] == 1 and second_number == numbers[base_counter]:
            continue
        return [base_counter+1, numbers_dict.get(second_number)["location"]+1]
    return []


def test_cases():
    list_of_cases = [
        {
            "s": [2,7,11,15],
            "t":9,
            "o": [1,2]
        },
        {
            "s": [2,3,4],
            "t":6,
            "o": [1,3]
        },
        {
            "s": [-1,0],
            "t":-1,
            "o": [1,2]
        },
    ]
    for case in range(len(list_of_cases)):
        output = two_sum(list_of_cases[case]["s"],list_of_cases[case]["t"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()