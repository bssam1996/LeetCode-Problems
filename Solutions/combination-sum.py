"""
Link: https://leetcode.com/problems/combination-sum/
"""


def combinationSum(candidates, target):
    # Memory limit exceeded
    from itertools import combinations_with_replacement
    r = int(target / min(candidates))
    all_possible_combinations = []
    for trial in range(1, r + 1):
        all_possible_combinations.append(list(combinations_with_replacement(candidates, trial)))
    output = []
    for test in all_possible_combinations:
        for item in test:
            summation = sum(item)
            if summation == target:
                output.append(list(item))
    return output


def test_cases():
    list_of_cases = [
        {
            "s": [2,3,6,7],
            "t":7,
            "o": [[2,2,3],[7]]
        },
        {
            "s": [2,3,5],
            "t":8,
            "o": [[2,2,2,2],[2,3,3],[3,5]]
        },
        {
            "s": [2],
            "t":1,
            "o": []
        },
    ]
    for case in range(len(list_of_cases)):
        output = combinationSum(list_of_cases[case]["s"],list_of_cases[case]["t"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()