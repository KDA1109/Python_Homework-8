import os


def input_contact():
    # f = open('data.txt', 'r')
    # if not f:
    #     f = open('data.txt', 'w')
    #     f.close()
    # else:
    #     f.close()
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w+')
        f.close()

    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите фамилию, имя и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1 - Имя\n2 - Фамилия\n3 - Телефон\n0 - Выход в главное меню')
        command_index = int(input('Команда: '))
        if command_index == 0:
            print('Выход из функции.')
            return
        elif str(command_index) not in '123':
            print('Других параметров нету.')

        else:
            data = input('Введите данные: ')
            print('Результат поиска: ')
            for contact in contacts:
                full_contact = contact.strip().split(';')
                if data in full_contact:
                    print(' '.join(full_contact))
            if data not in full_contact:
                print('Контакт не найден.')
            print('_' * 30)





def edit_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Сначала нужно найти контак в списке.')
        print('По каким параметрам ищем контакт?:\n1 - Фамилия\n2 - Имя\n3 - Телефон\n0 - Выход в главное меню')
        command_index = int(input('Команда: '))
        if command_index == 0:
            print('Выход из функции.')
            return
        elif str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            data = input('Введите данные: ')
            print('Результат поиска: ')
            for i, contact in enumerate(contacts):
                full_contact = contact.strip().split(';')
                if data in full_contact:
                    print(' '.join(full_contact))
                    print('_' * 30)
                    print('Какой параметр хотите изменить?:\n1 - Фамилия\n2 - Имя\n3 - Телефон\n4 - Все параметры\n0 - Назад')
                    field_index = int(input('Команда: '))
                    if field_index == 0:
                        break
                    if field_index == 1:
                        full_contact[0] = input('Введите новую фамилию: ')
                    elif field_index == 2:
                        full_contact[1] = input('Введите новое имя: ')
                    elif field_index == 3:
                        full_contact[2] = input('Введите новый телефон: ')
                    elif field_index == 4:
                        new_data = input('Введите новые данные через пробел (Фамилия, Имя, телефон): ')
                        full_contact = new_data.split()
                        contacts[i] = contact.replace(contact, ';'.join(full_contact) + '\n')
                        with open('data.txt', 'w', encoding='utf-8') as f:
                            f.writelines(contacts)
                        print('Контакт изменен.')
                        break
                    else:
                        print('Других параметров нету.')
                        break
                    contacts[i] = ';'.join(full_contact) + '\n'
                    with open('data.txt', 'w', encoding='utf-8') as f:
                        f.writelines(contacts)
                    print('Контакт изменен.')
                    break
            else:
                print('Контакт не найден.')
            print('_' * 30)

def dell_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Сначала нужно найти контак в списке.')
        print('По каким параметрам ищем контакт?:\n1 - Имя\n2 - Фамилия\n3 - Телефон\n0 - Выход в главное меню')
        command_index = int(input('Команда: '))
        if command_index == 0:
            print('Выход из функции.')
            return
        elif str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            data = input('Введите данные: ')
            print('Результат поиска: ')
            for i, contact in enumerate(contacts):
                full_contact = contact.strip().split(';')
                if data in full_contact:
                    print(' '.join(full_contact))
                    confirm = input('Удалить контакт? (y/n): ')
                    if confirm.lower() == 'y':
                        del contacts[i]
                        with open('data.txt', 'a', encoding='utf-8') as f:
                            f.writelines(contacts)
                        print('Контакт удален.')
                    else:
                        print('Контакт не удален.')
                    break
            else:
                print('Контакт не найден.')
            print('_' * 30)





