'''
Link: https://leetcode.com/problems/three-divisors/
'''


def isThree(n):
    list_of_possibilities = [1]
    for counter in range(2, int(n / 2) + 1):
        if n % counter == 0:
            list_of_possibilities.append(counter)
        if len(list_of_possibilities) == 3:
            break
    list_of_possibilities.append(n)
    return True if len(list_of_possibilities) == 3 else False


# n = 2
# O = False

n = 4
# O = True

print(isThree(n))