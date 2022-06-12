"""
Link: https://leetcode.com/problems/n-th-tribonacci-number/
"""


def tribonacci(n: int):
    dp = [0] * max(3,(n + 1))
    dp[1] = 1
    dp[2] = 1
    if n < 3:
        return dp[n]
    for i in range(3,n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


def test_cases():
    list_of_cases = [
        {
            "s": 25,
            "o": 1389537
        },
        {
            "s": 4,
            "o": 4
        },
    ]
    for case in range(len(list_of_cases)):
        output = tribonacci(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)

test_cases()

