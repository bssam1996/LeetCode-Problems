"""
Link: https://leetcode.com/problems/number-of-boomerangs/
"""


def is_boomerang(point):
    first_point_x = point[0][0]
    first_point_y = point[0][1]
    second_point_x = point[1][0]
    second_point_y = point[1][1]
    third_point_x = point[2][0]
    third_point_y = point[2][1]
    first_distance = ((second_point_x - first_point_x)**2 + (second_point_y - first_point_y)**2)**0.5
    second_distance = ((third_point_x - first_point_x)**2 + (third_point_y - first_point_y)**2)**0.5
    return first_distance == second_distance


def numberOfBoomerangs(points):
    if len(points) < 3:
        return 0
    from itertools import permutations
    all_possible_permutations = permutations(points, 3)
    boomerangs_counter = 0
    for point in all_possible_permutations:
        boomerangs_counter += 1 if is_boomerang(point) else 0
    return boomerangs_counter


def test_cases():
    list_of_cases = [
        {
            "s": [[0,0],[1,0],[2,0]],
            "o": 2
        },
        {
            "s": [[1,1],[2,2],[3,3]],
            "o": 2
        },
        {
            "s": [[1, 1]],
            "o": 0
        },

    ]
    for case in range(len(list_of_cases)):
        output = numberOfBoomerangs(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()
