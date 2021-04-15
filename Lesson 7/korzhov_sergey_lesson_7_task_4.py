import os

django_path = r'my_project\django'  # Разместил файлы фреймворка в папке my_project

file_stat = {}  # Словарь со статистикой
n = 4  # По необходимости интервалами можно управлять

interval_list = [[0,100]]  # Соберем интервалы для статистики
file_stat.update({100: 0})  # Сразу начнем заполнять словарь, потом просто обновлеям

for i in range(1, n):
    interval_list.append([interval_list[i-1][1]+1, interval_list[i-1][1] * 10])
    file_stat.update({interval_list[i][1]: 0})


def get_interval(size):
    for el in interval_list:
        if el[0] <= size <= el[1]:
            yield el[1]


def add_file(key=None):
    if key is not None:  # Исключаем файлы, которые больше последнего интервала
        file_stat[key] += 1


for root, dirs, files in os.walk(django_path):
    for file in files:
        file_size = os.stat(os.path.join(root,file)).st_size
        g = get_interval(file_size)
        add_file(*g)

print(file_stat)
