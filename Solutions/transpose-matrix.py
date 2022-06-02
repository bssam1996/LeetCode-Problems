"""
Link: https://leetcode.com/problems/transpose-matrix/
"""


def transpose(matrix):
    new_list = []
    for element in range(len(matrix[0])):
        new_column = []
        for row in range(len(matrix)):
            new_column.append(matrix[row][element])
        new_list.append(new_column)
    return new_list


def transpose2(matrix):
    # Triple time and Double Space
    import numpy
    return numpy.transpose(matrix).tolist()


def test_cases():
    list_of_cases = [
        {
            "s": [[1,2,3],[4,5,6],[7,8,9]],
            "o": [[1,4,7],[2,5,8],[3,6,9]]
        },
        {
            "s": [[1,2,3],[4,5,6]],
            "o": [[1,4],[2,5],[3,6]]
        },
    ]
    for case in range(len(list_of_cases)):
        output = transpose2(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()

# print(transpose(nums))
