import itertools
from sys import argv


def write_file(users_list, hobby_list, fw):
    if len(users_list) < len(hobby_list):  # По ТЗ должны выдать ошибку
        raise ValueError('Ошибка формирования')
    else:
        for user, hobby in itertools.zip_longest(users_list, hobby_list, fillvalue=None):
            fw.write(f'{user}: {hobby}\n')


def get_date(f):
    date_list = []
    with open(f, 'r', encoding='utf-8') as f:
        lines = (el for el in f.readlines())
        for line in lines:
            date_list.append(line)
        date_list = list(map(lambda el: el.replace('\n', ''), date_list))

        return date_list


def read_files(file_users, file_hobby, file_result):
    users_list = get_date(file_users)
    hobby_list = get_date(file_hobby)
    with open(file_result, 'w', encoding='utf-8') as wf:
        write_file(users_list, hobby_list, wf)


if __name__ == '__main__':
    _script, f_users, f_hobby, f_result = argv
    read_files(f_users, f_hobby, f_result)

