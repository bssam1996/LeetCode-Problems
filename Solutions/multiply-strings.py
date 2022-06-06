"""
Link: https://leetcode.com/problems/multiply-strings/
"""


def multiply(num1, num2):
    first_number = 0
    for element in range(len(num1)):
        first_number += 10**element * int(num1[len(num1)-element-1])
    second_number = 0
    for element in range(len(num2)):
        second_number += 10 ** element * int(num2[len(num2) - element - 1])
    output = first_number * second_number
    return str(output)

multiply("23","3")