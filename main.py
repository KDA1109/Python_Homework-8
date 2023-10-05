from logger import input_contact, print_contacts, find_contact, edit_contact, dell_contact


def menu():
    text = '' \
           "Главное меню:\n" \
           "0 - Завершить работу\n"\
           "1 - Добавить контакт\n" \
           "2 - Посмотреть все контакты\n" \
           "3 - Найти контакт\n"\
           "4 - Редактировать коктакт\n"\
           "5 - Удалить контакт\n"\
           ""

    print(text)
    while True:
        comand = int(input('Введите команду: '))
        if comand == 1:
            input_contact()
        if comand == 2:
            print('Список контактов:')
            print_contacts()
        if comand == 3:
            find_contact()
        if comand == 4:
            edit_contact()
        if comand == 5:
            dell_contact()
        if comand == 0:
            print('Спасибо за работу!')
            break
        print('_' * 30)


if __name__ == '__main__':
    menu()
