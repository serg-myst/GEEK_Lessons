import os
from pathlib import Path
import json

django_path = r'my_project\django'  # Разместил файлы фреймворка в папке my_project

file_stat = {}  # Словарь со статистикой
result_dict = {}  # Словарь для вывода результата
n = 4  # По необходимости интервалами можно управлять

interval_list = [[0,100]]  # Соберем интервалы для статистики
file_stat.update({100: [0, []]})
result_dict.update({100: ()})

for i in range(1, n):
    interval_list.append([interval_list[i-1][1]+1, interval_list[i-1][1] * 10])
    file_stat.update({interval_list[i][1]: [0, []]})
    result_dict.update({interval_list[i][1]: ()})


def get_interval(size):
    for el in interval_list:
        if el[0] <= size <= el[1]:
            yield el[1]


def add_file(key=None, file_type=''):
    if key is not None:  # Исключаем файлы, которые больше последнего интервала
        file_stat[key][0] += 1  # Здесь у нас счетчик файлов
        if file_type not in file_stat[key][1]:
            file_stat[key][1].append(file_type)


for root, dirs, files in os.walk(django_path):
    for file in files:
        file_size = os.stat(os.path.join(root,file)).st_size
        g = get_interval(file_size)
        add_file(*g, Path(os.path.join(root,file)).suffix.replace('.',''))

for k, i in file_stat.items():
    result_dict[k] = i[0], i[1]

print(result_dict)  # Покажем на экран результат

with open('lesson7_summary.json', 'w', encoding='utf-8') as wf:
    json.dump(result_dict, wf)