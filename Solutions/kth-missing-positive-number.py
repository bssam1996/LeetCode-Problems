"""
Link: https://leetcode.com/problems/kth-missing-positive-number/
"""


def findKthPositive(arr, k):
    original_k = k
    current = 1
    first_element = arr[0]
    values = [i+1 for i in range(0,first_element-1)]
    while k > 0:
        for element_index in range(current,len(arr)):
            for i in range(arr[element_index - 1]+1, arr[element_index]):
                values.append(i)
                k -= 1
        current = len(arr)
        if len(values) == 0:
            values.append(arr[-1] + 1)
        elif arr[-1] > values[-1]:
            values.append(arr[-1] + 1)
        else:
            values.append(values[-1] + 1)
        k -= 1
    return values[original_k-1]


def findKthPositive2(arr, k):
    list1 = []
    last_element = arr[-1]
    arr = set(arr)
    num_elements = k
    for i in range(1, last_element + k + 1):
        if i not in arr:
            num_elements -= 1
            list1.append(i)
        if num_elements == 0:
            break
    return list1[k - 1]
#
# arr = [2,3,4,7,11]
# k = 5

# arr = [1,2,3,4]
# k = 2

# arr = [5,6,7,8,9]
# k = 9

arr = [1,13,18]
k = 17

print(findKthPositive2(arr, k))