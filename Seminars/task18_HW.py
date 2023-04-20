# Задача 18: 

# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

number = int(input(('Введите натуральное число N ')))
array = []

for i in range(number): 
    temp = random.randint(1, number)
    array.append(temp)
print(array)

x = int(input(('Введите число X ')))
diff = 0

array_diff = []
for i in array:
    diff = i - x
    diff_all_positive = abs(diff)
    # print()
    # print(diff_all_positive)
    array_diff.append(diff_all_positive)
print(array_diff)


new_min = min(array_diff)
print(new_min)


answer_number = x - new_min
print(answer_number)

# __________________________________________________________________

# import random

# number = int(input(('Введите натуральное число N ')))
# array = []

# for i in range(number): 
#     temp = random.randint(1, number)
#     array.append(temp)
# print(array)

# x = int(input(('Введите число X ')))
# diff = 0

# if x in array:
#     print(x) 

# count = 0
# for i in array:
#     if i == x + 1:
#         print(i)
#         count += 1
#     if i == x - 1:
#         print(i)
#         count += 1