# Задача 30: 

# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Введите первый элемент: '))
k = int(input('Введите кол-во элементов: '))
d = int(input('Введите разность: '))
array = []

for i in range(6):
    if i > 0:
        a_new = a + (i - 1) * d
        array.append(a_new)
print(array)