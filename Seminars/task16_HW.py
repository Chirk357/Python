# Задача 16: 

# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

import random

number = int(input(('Введите натуральное число N ')))
array = []

for i in range(number): 
    temp = random.randint(1, number)
    array.append(temp)
print(array)

x = int(input(('Введите число X ')))
count = 0


for i in range(0, len(array)):
    if x == array[i]:
        count += 1
print(count)




