"""
Link: https://leetcode.com/problems/prime-palindrome/
"""


def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for counter in range(2, int(number**0.5) + 1):
        if number % counter == 0:
            return False
    return True


def isPalingdrome(number):
    number_string = str(number)
    if len(number_string) == 1:
        return True
    if len(number_string) % 2 == 1:
        number_string = number_string[0:int(len(number_string)/2)] + number_string[int(len(number_string)/2)+1:]
    first_half = number_string[0:int(len(number_string)/2)]
    second_half = number_string[-1:int(len(number_string)/2)-1:-1]
    return first_half == second_half


def primePalindrome(n):
    while n:
        if isPalingdrome(n) and isPrime(n):
            return n
        n += 1
        if 10 ** 7 < n < 10 ** 8:
            n = 10 ** 8


def test_cases():
    list_of_cases = [
        {
            "s": 6,
            "o": 7
        },
        {
            "s": 8,
            "o": 11
        },
        {
            "s": 13,
            "o": 101
        },
        {
            "s": 1215122,
            "o": 1218121
        },
        {
            "s":1437342,
            "o":1444441
        },
        {
            "s":9989900,
            "o":100030001
        },
        {
            "s":85709140,
            "o":100030001
        }
    ]
    for case in range(len(list_of_cases)):
        output = primePalindrome(list_of_cases[case]["s"])
        result = (output == list_of_cases[case]["o"])
        print("#", case, result)
        if not result:
            print("Expected Output", list_of_cases[case]["o"])
            print("Actual Output", output)


test_cases()

