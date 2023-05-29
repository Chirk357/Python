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


def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list

def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)



def search_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    # print(len(adr_book))
    # for i in range(len(adr_book)):
    #     print(i, adr_book[i])
    # idx = int(input('Введи индекс для замены: '))
    # last_name, name, _ = adr_book[idx].split('; ')
    # phone = input('новый номер: ')
    # new_record = f'{last_name}; {name}; {phone}'
    # adr_book[idx] = new_record
    # with open(f, 'w', encoding='utf-8') as fd:
    #     fd.writelines(adr_book)
    find_list = []
    for line in adr_book:
        if last_name in line:
            find_list.append(line)
    if find_list is None:
        print('не найден')
        
    else:
        for find_line in find_list:
            print(find_line)
        



def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книгу,\n'
                            '3 - найти запись,\nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break

if __name__ == '__main__':
    main()