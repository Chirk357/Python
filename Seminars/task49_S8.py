# Задача №49. 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейнойopen mode
# mode, open, encoding

# with open('file.txt', 'w', encoding='utf-8') as fd: #with ...as потом закроет файл сам. fd это переменная название файла = file descripter
#     fd.write('первая строка в этом файле') #fd.write используем для обращения к этому файлу

# with open('file.txt', 'w', encoding='utf-8') as fd:
#     fd.write('\n2я строка в этом файле')  #\n перенос строки

# with open('file.txt', 'r', encoding='utf-8') as file:
#     z = file.read() # записали файл в переменную
#     print(z)
#     z = fd.readlines()
#     for i in z:
#         print(i)


import methods as mt 

def main(): 
    file = 'address_book.txt' 
    while True: 
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книжку,\n' 
                            '3 - найти запись,\n4 - очистить данные, \nz - для выхода: ') 
        if user_choice == '1': 
            mt.add_contact(file) 
        elif user_choice == '2': 
            mt.print_all(file) 
        elif user_choice == '3': 
            mt.search_contact(file) 
        elif user_choice == '4': 
            mt.clear_phone_book(file) 
        elif user_choice == 'z' or 'Z': 
            print('Всего доброго!') 
            break 

if __name__ == '__main__': 
    main()


