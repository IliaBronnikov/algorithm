'''
Write a function two_sum(nums, target) that takes a list nums and an integer target. The function should return the indices of the two numbers in the list that add up to give target.

If there are no such numbers, the function should return None.

print(two_sum([2, 7, 11, 15], 9))  # Вывод: [0, 1]
'''

def two_sum(nums, target):
    hash_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], index]
        hash_map[num] = index

    return None
