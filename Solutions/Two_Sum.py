'''
Link: https://leetcode.com/problems/two-sum/
'''


def two_sum(nums, target):
    for base_counter in range(len(nums) - 1):
        for moving_counter in range(base_counter + 1, len(nums)):
            if nums[base_counter] + nums[moving_counter] == target:
                return [base_counter, moving_counter]
    return []


def two_sum2(nums, target):
    numbers = {}
    for base_counter in range(len(nums)):
        if numbers.get(nums[base_counter]) is None:
            numbers[nums[base_counter]] = {
                "counter": 1,
                "location": base_counter
            }
        else:
            numbers[nums[base_counter]]["counter"] += 1
            numbers[nums[base_counter]]["location"] = base_counter
    for base_counter in range(len(nums)):
        second_number = target - nums[base_counter]
        if numbers.get(second_number) is None:
            continue
        if numbers.get(second_number)["counter"] == 1 and second_number == nums[base_counter]:
            continue
        return [base_counter, numbers.get(second_number)["location"]]
    return []

def two_sum3(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [i, seen[remaining]]

        seen[value] = i
    return []

nums = [3,2,4]
target = 6
print(two_sum2(nums, target))
