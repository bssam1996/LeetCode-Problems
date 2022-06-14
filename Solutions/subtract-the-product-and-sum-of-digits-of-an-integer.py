"""
Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
"""


def subtractProductAndSum(self, n: int) -> int:
    total_sum = 0
    total_product = 1
    n = str(n)
    for number in n:
        total_sum += int(number)
        total_product *= int(number)

    return int(total_product - total_sum)