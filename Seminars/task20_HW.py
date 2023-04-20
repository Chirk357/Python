# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12


letter_score_dict = {'AEIOULNSTR': 1, 
                'DG': 2, 
                'BCMP': 3,
                'FHVWY': 4, 
                'K': 5, 
                'JX': 8, 
                'QZ': 10,
                'АВЕИНОРСТ': 1,
                'ДКЛМПУ': 2,
                'БГЁЬЯ': 3,
                'ЙЫ': 4,
                'ЖЗХЦЧ': 5,
                'ШЭЮ': 8,
                'ФЩЪ': 10}
def word_score(letter_score_dict, word):
    total_score = 0
    for letter in word:
        for v_key, v_value in letter_score_dict.items():
            if letter.upper() in v_key:
                total_score += v_value
    return total_score

word = input('Введите слово: ')
print(f'{word_score(letter_score_dict, word)}')

# for item in English_dict:
#     print('{}: {}'. format(item, English_dict[item]))

# for item in Russian_dict:
#     print('{}: {}'. format(item, Russian_dict[item]))

