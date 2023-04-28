# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:               Вывод:
# 7                   3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1      (каждое число вводится с новой строки)

def nums_list(n):
    result_list = []
    for i in range(n):
        result_list.append(int(input('Введите элемент: ')))
    return result_list

# print(nums_list(7))


def create_list():
    list_1 = input('Введите эл-ты массива через пробел').split() #разделить числа через пробел
    # print(list_1)

    for k in range(len(list_1)):
        list_1 [k]= int(list_1[k])  # превращение строки ['7', '8', '7', '6', '8', '9', '7'] в числа целые [7, 8, 7, 6, 8, 9, 7]
    return list_1



def short_list(list_1, list_2):
    list_c = []
    for i in list_a: # i это не индекс, а элемент
        if i not in list_b:
            list_c.append(i)
    return list_c

list_a = [3, 1, 3, 4, 2, 4, 12]
list_b = [4, 15, 43, 1, 15, 1]

print(short_list(list_a, list_b))

#___________________

# def short_list(*args):
#     list_a, list_b = args
#     list_c = []
#     for i in list_a: # i это не индекс, а элемент
#         if i not in list_b:
#             list_c.append(i)
#     return list_c
