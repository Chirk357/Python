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

c = int(input("Введите длину массива: "))

d = [] 

# e = int(input("Введите число: "))

for i in range(c): 

    temp2 = random.randint(0, 9)

    d.append(temp2)

print(d)

e = int(input("Введите число: "))

g1=abs(d[0]-e) 

temp3 = d[0]

dif18 = 0

for i in range(len(d)):

    if d[i]==e:

        temp3 = d[i] 

        break           

    if d[i]<e:

        dif18=e-d[i]

    if d[i]>e:

        dif18=d[i]-e

    if dif18<g1:

        g1=dif18

        temp3 = d[i]

print(temp3)



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