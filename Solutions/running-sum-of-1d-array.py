"""
Link: https://leetcode.com/problems/running-sum-of-1d-array/
"""


def runningSum(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        nums[i] = sum
    return nums


def test_cases():
    list_of_cases = [
        {
            "s": [1,2,3,4],
            "o": [1,3,6,10]
        },
        {
            "s":[1,1,1,1,1],
            "o":[1,2,3,4,5]
        },
        {
            "s":[3,1,2,10,1],
            "o":[3,4,6,16,17]
        }

    ]
    for case in range(len(list_of_cases)):
        output = runningSum(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()
