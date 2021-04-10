import itertools


def write_file(users_list, hobby_list):
    if len(users_list) < len(hobby_list):  # По ТЗ должны выдать ошибку
        raise ValueError('Ошибка формирования')
    else:
        with open('users_hobby.txt', 'w', encoding='utf-8') as wf:
            for user_name, user_hobby in itertools.zip_longest(users_list, hobby_list, fillvalue=None):
                wf.write(f'{user_name}: {user_hobby}\n')


def get_date(file_name):
    date_list = []
    with open(file_name, 'r', encoding='utf-8') as fr:
        lines = (el for el in fr.readlines())
        for line in lines:
            date_list.append(line)
        date_list = list(map(lambda el: el.replace('\n', ''), date_list))

        return date_list


users = get_date('users.csv')
hobby = get_date('hobby.csv')
write_file(users, hobby)
