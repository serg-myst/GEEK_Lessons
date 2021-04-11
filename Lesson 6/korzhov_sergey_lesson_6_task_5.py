import itertools
from sys import argv


def write_file(users_list, hobby_list, fw):
    if len(users_list) < len(hobby_list):  # По ТЗ должны выдать ошибку
        raise ValueError('Ошибка формирования')
    else:
        for user, hobby in itertools.zip_longest(users_list, hobby_list, fillvalue=None):
            fw.write(f'{user}: {hobby}\n')


def get_data(f):
    data_list = []
    with open(f, 'r', encoding='utf-8') as f:
        lines = (el for el in f.readlines())
        for line in lines:
            data_list.append(line)
        data_list = list(map(lambda el: el.replace('\n', ''), data_list))

        return data_list


def read_files(file_users, file_hobby, file_result):
    users_list = get_data(file_users)
    hobby_list = get_data(file_hobby)
    with open(file_result, 'w', encoding='utf-8') as wf:
        write_file(users_list, hobby_list, wf)


if __name__ == '__main__':
    _script, f_users, f_hobby, f_result = argv
    read_files(f_users, f_hobby, f_result)

