# Задача 26:  

# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('Введите число '))
b = int(input('Введите введите степень числа '))

def stepen(a, b):
    if a == 0 or b == 0:
        return 1
    if b == 1:
        return a
    return a * stepen(a, b-1)


print(stepen(a, b))