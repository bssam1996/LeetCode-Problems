"""
Link: https://leetcode.com/problems/search-insert-position/
"""


def searchInsert(nums, target):
    # Binary Search
    left = 0
    right = len(nums) - 1
    mid = left + int((right - left) / 2)
    while left < right:
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            left = mid
            break
        else:
            right = mid - 1
        mid = left + int((right - left) / 2)
    if target <= nums[left]:
        return left
    return left + 1


def test_cases():
    list_of_cases = [
        {
            "s": [1,3,5,6],
            "t": 5,
            "o": 2
        },
        {
            "s": [1, 3, 5, 6],
            "t": 2,
            "o": 1
        },
        {
            "s": [1,3,5,6],
            "t": 7,
            "o": 4
        },
    ]
    for case in range(len(list_of_cases)):
        output = searchInsert(list_of_cases[case]["s"], list_of_cases[case]["t"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


# print(searchInsert([1,3,5,6],7))
test_cases()
