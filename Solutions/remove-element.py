"""
Link: https://leetcode.com/problems/remove-element/
"""


def removeElement(nums, val):
    counter = 0
    while counter < len(nums):
        if nums[counter] == val:
            del nums[counter]
            counter -= 1
        counter += 1
    return len(nums)


def test_cases():
    list_of_cases = [
        {
            "s": [3,2,2,3],
            "t": 3,
            "o": 2
        },
        {
            "s": [0,1,2,2,3,0,4,2],
            "t": 2,
            "o": 5
        },

    ]
    for case in range(len(list_of_cases)):
        output = removeElement2(list_of_cases[case]["s"], list_of_cases[case]["t"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(searchInsert([1,3,5,6],7))
test_cases()
