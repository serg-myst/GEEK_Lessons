import itertools
import json


def write_file(users_list, hobby_list):
    dct = {}
    if len(users_list) < len(hobby_list):  # По ТЗ должны выдать ошибку
        raise ValueError('Ошибка формирования')
    else:
        for user, hobby in itertools.zip_longest(users_list, hobby_list, fillvalue=None):
            dct.update({user: hobby})
        print(dct)  # Покажем, что это словарь
        with open('my_file.txt', 'w', encoding='utf-8') as wf:
            json.dump(dct, wf)  # Сериализуем объект


with open('users.csv', 'r', encoding='utf-8') as f:
    users = list(map(lambda el: el.replace('\n', '').replace(',', ' '), f.readlines()))

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = list(map(lambda el: el.replace('\n', ''), f.readlines()))

write_file(users, hobby)

# Проверим, что в файл записали словарь
try:
    with open('my_file.txt','r',encoding='utf-8') as f:
        print(f'Сохраненный выше объект = {type(json.load(f))}')
except:
    print('Ошибка чтения файла.')
