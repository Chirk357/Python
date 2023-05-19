# Задача №49. 
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

import math

def find_farthest_orbit(orbits):
    orb_filter = list(filter(lambda x: x[0] != x[1], orbits))
    print (orb_filter)
    s = []
    max_sq = orb_filter[0][0] * orb_filter[0][1] * math.pi
    res = None

    for i in range(len(orb_filter)):
        dif_sq = orb_filter[i][0] * orb_filter[i][1] * math.pi #import math --> math.pi - это число Пи ипортированное из библиотеки
        #orb_filter[i][0] * orb_filter[i][1] - это 1, 3 при i = 0; при i = 1, 2.5 и 10 - это элементы под индексом [0] и [1]
        if max_sq < dif_sq:
            max_sq = dif_sq
            res = i

    return orb_filter[res]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))

# _________________________________________________________

# def find_farthest_orbit(orbits):
#     for orbit in orbits:
#         if orbit[0] * orbit[1] * pi == max(map(lambda orb_tupl: orb_tupl[0] * orb_tupl[1] * pi,
#                                                filter(lambda x: x[0] != x[1], orbits))):
#             return orbit



#_____________________________________________________________
from math import pi

def find_farthest_orbit(orbits):
    res_list = [i for i in orbits if i[0] * i[1] * pi == max(
        map(lambda orb_tupl: orb_tupl[0] * orb_tupl[1] * pi,
            filter(lambda x: x[0] != x[1], orbits))
    )]
    # print(type(res_list))
    return res_list[0]
    # [(2.5, 10)] - res_list
    # (2.5, 10) - res_list[0]
    # for orbit in orbits:
    #     if orbit[0] * orbit[1] * pi == max(map(lambda orb_tupl: orb_tupl[0] * orb_tupl[1] * pi,
    #                                            filter(lambda x: x[0] != x[1], orbits))):
    #         return orbit
    # orb_filter = list(filter(lambda x: x[0] != x[1], orbits))
    # maxx = orb_filter[0][0] * orb_filter[0][1] * pi
    # max_t = orb_filter[0]
    # for i in orb_filter:
    #     if i[0] * i[1] * pi > maxx:
    #         maxx = i[0] * i[1] * pi
    #         max_t = i
    # return max_t


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# final_res = find_farthest_orbit(orbits)
# print(final_res)
# print(type(final_res))
# print(*final_res)
# for i in orbits:
#     if i[0] != i[1]:
#         print(i)
# res_list = [i for i in orbits if i[0] != i[1]]
# print(res_list)

# res_list = [i for i in orbits if i[0] * i[1] * math.pi == max(map(lambda orb_tupl:
#                                                     orb_tupl[0] * orb_tupl[1] * math.pi,
#                                                   filter(lambda x: x[0] != x[1], orbits)))                             ]
#     return res_list