def add_contact(f): 
    input_last_name = input('Введите Фамилию: ').capitalize() 
    input_name = input('Введите Имя: ').capitalize() 
    input_phone = input('Введите номер телефона: ') 
    data = f'{input_last_name}; {input_name}; {input_phone}' 
    with open(f, 'a', encoding='utf-8') as pd: 
        pd.write(f'{data}\n') 
    print(f'Запись {data} добавлена\n') 


def read_all(f): 
    with open(f, 'r', encoding='utf-8') as fp: 
        file_list = fp.readlines() 
        return file_list 


def print_all(f): 
    adr_book = read_all(f) 
    if not adr_book: 
        print('Книжка пуста') 
    else: 
        for line in adr_book: 
            new_ = line.replace(';', '') 
            new_ = new_.replace('\n', '') 
            print(new_) 
    print() 


def search_contact(f): 
    adr_book = read_all(f) 
    if not adr_book: 
        print('Записей нет!\n') 
    else: 
        for i in range(len(adr_book)): 
            print(f'{i+1} - {adr_book[i]}') 
        idx = int(input('Укажите индекс для замены: ')) - 1 
        par_choice = input('Укажите, что хотите изменить: 1 - Фамилию, 2 - Имя, 3 - Номер телефона -- ') 
        last_name, name, phone = adr_book[idx].split(';') 
        #print(last_name, name, phone) 
        if par_choice == '1': 
            last_name = input('Укажите новую фамилию: ').capitalize() 
        elif par_choice == '2': 
            name = input('Укажите новое имя: ').capitalize() 
        elif par_choice == '3': 
            phone = input('Укажите новый номер телефона: ').capitalize() 
        else: 
            print('Некорректный ввод') 
        print(last_name, name, phone) 
        new_record = f'{last_name}; {name}; {phone}' 
        adr_book[idx] = new_record 
        #print(adr_book[idx]) 
        with open(f, 'w', encoding='utf-8') as pp: 
            pp.writelines(adr_book) 
        print() 


def clear_phone_book(f): 
    adr_book = read_all(f) 
    if not adr_book: 
        print('Книжка и так пуста!\n') 
    else: 
        act_choice = input('Выберите действие: 1 - очистить книжку, 2 - удалить контакт ') 
        if act_choice == '1': 
            adr_book.clear() 
        elif act_choice == '2': 
            for i in range(len(adr_book)): 
                print(f'{i+1} - {adr_book[i]}') 
            idx = int(input('Укажите номер контакта, который хотите удалить: ')) - 1 
            del adr_book[idx] 
        with open(f, 'w', encoding='utf-8') as fw: 
            fw.writelines(adr_book) 
            print('Данные удалены!\n')