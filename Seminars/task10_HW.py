# Задача 10: 

# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

monneti = int(input(('Введите кол-во монет ')))
orel_reshka = []
count_orel = 0
count_reshka = 0

for i in range(monneti): 
    temp = random.randint(0, 1)
    orel_reshka.append(temp)
print(orel_reshka)

for i in orel_reshka:
    if i == 1:
        count_orel += 1
print('Монеты, перевернутые вверх орлом', count_orel)

for i in orel_reshka:
    if i == 0:
        count_reshka += 1
print('Монеты, перевернутые вверх решкой', count_reshka)

if count_orel > count_reshka:
    print('Надо перевернуть монеты решкой', count_reshka)
else:
    print('Надо перевернуть монеты с орлом', count_orel)