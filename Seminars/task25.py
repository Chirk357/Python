# Задача №25. 

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



my_list = 'a a a b c a a d c d d'.split()
result_str = ''
for i in range(len(my_list)):
    print(my_list[:i])
    print(my_list[:i].count(my_list[i]))
    print('-' * 15)
    if len(result_str) == 0:
        result_str = my_list[i]
    elif my_list[:i].count(my_list[i]) == 0:
        result_str += ' ' + my_list[i]
    else:
        result_str += ' _' + my_list[i] + str(my_list[:i].count(my_list[i]))

print(result_str)
    

# string = "a a a b c a a d c d d" #первый способ
# dict_new = {}
# for char in string.split():
#     if char in dict_new: # char строковая переменная
#         dict_new[char] += 1 # если эта буква попадается со ставим 1. Так как неменяемая переменная , то переаписываем
#         char += "_" + str(dict_new[char])
#     else:
#         dict_new[char] = 0   #создаем ключ и ставим туда 0

#     print(char, end=" ")