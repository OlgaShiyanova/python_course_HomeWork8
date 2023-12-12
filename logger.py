# open('test.txt')
def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end='\n\n')
        else:
            print('Список контактов пустой')


def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info


def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)


def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print("Выберите критерий для поиска:" +
    '1 - Имя' +
    '2 - Фамилия' +
    '3 - Телефон'
    )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)

def find_contact_number(file_name, n):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    
    count = 0
    for cont in all_cont:
        count = count + 1
        if count == n:
            return cont

def copy_contact(file_name, file_new):
    print('Введите номер строки контакта')
    num = int(input())
    copycont = find_contact_number(file_name, num)
    
    with open(file_new, 'w', encoding='utf8') as file:
        file.writelines(copycont)