"""
Link: https://leetcode.com/problems/sum-of-square-numbers/
"""


def judgeSquareSum(c):
    def isSqrt(number):
        return number ** 0.5, (number**0.5 - int(number**0.5)) == 0

    for i in range(1,int(c/2)):
        sqrt, perfect = isSqrt(i)
        if perfect:
            second_sqrt, second_perfect = isSqrt(c-sqrt)
            if second_perfect:
                return True
    return False

print(judgeSquareSum(5))

