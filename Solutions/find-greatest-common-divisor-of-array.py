'''
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
'''


def gcd(nums):
    nums.sort()
    smallest = nums[0]
    largest = nums[-1]
    list_of_possibilities = [1]
    for counter in range(2, int(smallest / 2)+1):
        if smallest % counter == 0:
            list_of_possibilities.append(counter)
    list_of_possibilities.append(smallest)
    for value in list_of_possibilities[-1::-1]:
        if largest % value == 0:
            return value
    return 0


nums = [2, 4, 6, 7, 8, 10]
# O = 2

# nums = [7, 5, 6, 8, 3]
# O = 1

# nums = [3, 3]
# O = 3

# nums = [6, 7, 9]
# O = 3
print(gcd(nums))
