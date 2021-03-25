
def my_func(*args):

    my_dict = {}

    for last_name in args:
        # Первая буква фамилии - word_lv1
        # Фамилии, начинающиеся с буквы word_lv1, получаем filter(lambda el: el.split()[-1:][0][:1] == word_lv1, args)
        word_lv1 = last_name.split()[-1:][0][:1]
        list_lv1 = list(filter(lambda el: el.split()[-1:][0][:1] == word_lv1, args))

        my_dict_lv1 = {}

        for name in list_lv1:
            # В полученном выше списке соберем словарь по именам сотрудников как в задаче 3
            my_dict_lv1.update({name[:1]: list(filter(lambda el: el[:1] == name[:1], list_lv1))})

        my_dict.update({word_lv1: my_dict_lv1})

    return my_dict


result = my_func('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Иосиф Индюков', 'Валентин Илюшин',
                 'Анна Савельева', 'Семен Альтов')
print(result)

# Отсортируем словарь по ключам. Воспользуемся встроенной функцией sorted()
# Полученный результат - новый объект Список. Обернем его обратно в словарь dict()
print('Отсортированный по ключам словарь')
print(dict(sorted(result.items())))