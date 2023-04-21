# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def nums_replace(nums):
    temp_min = min(nums)
    temp_max = max(nums)
    for i in range(len(nums)):
        if nums[i] == temp_max:
            nums[i] = temp_min
    return nums

print(*nums_replace([1, 3, 3, 3, 4]))