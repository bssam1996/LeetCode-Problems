"""
Link: https://leetcode.com/problems/median-of-two-sorted-arrays
"""


def findMedianSortedArrays(nums1, nums2):
    nums1_length = len(nums1)
    nums2_length = len(nums2)
    special_case = nums1_length == 0 or nums2_length == 0
    if nums1_length == 0:
        new_array = nums2
    if nums2_length == 0:
        new_array = nums1
    if nums1_length == 0 and nums2_length == 0:
        return []
    if special_case:
        total_length = len(new_array)
        even = total_length % 2 == 0
        if even:
            middle = int(total_length / 2 - 1)
            return (new_array[middle] + new_array[middle + 1]) / 2
        else:
            middle = int(total_length / 2)
            return float(new_array[middle])
    total_length = nums1_length + nums2_length
    even = True
    if total_length % 2 == 1:
        even = False
    limit = total_length / 2
    start1 = 0
    start2 = 0
    current_value = []
    for total_counter in range(0, int(limit) + 1):
        if nums1_length == start1:
            current_value.append(nums2[start2])
            start2 += 1
            continue
            # num1_value = nums1[start1 - 1]
        else:
            num1_value = nums1[start1]
        if nums2_length == start2:
            current_value.append(nums1[start1])
            start1 += 1
            continue
        else:
            num2_value = nums2[start2]
        if num1_value < num2_value:
            current_value.append(num1_value)
            start1 += 1
        else:
            current_value.append(num2_value)
            start2 += 1
    print(current_value)
    if even:
        return (current_value[-1] + current_value[-2]) / 2
    return float(current_value[-1])


# nums1 = [1,4,7,9]
# nums2 = [2,3,5]

# nums1 = [1,4,7,9]
# nums2 = [2,3,5,6,8]

nums1 = [1,3]
nums2 = [2]


# nums1 = [1,4,7,9, 10, 11, 17,19] # 9
# nums2 = [2,3,5,6,8,12,13,14,15]

# nums1 = [1,4,7,9, 10, 11, 17] ## 8.5
# nums2 = [2,3,5,6,8,12,13,14,15]
# print(sorted(nums1 + nums2))
# print(len(nums1 + nums2))


# nums1 = [1,2]
# nums2 = [3,4]


# nums1 = [1,2]
# nums2 = []

# nums1 = [2,3,4]
# nums2 = [1]

# nums1 = [9]
# nums2 = [1,2,3,4]

# nums1 = []
# nums2 = [1,2,3,4]
print(findMedianSortedArrays(nums1,nums2))