
def my_func(*args):
    my_dict = {}
    for name in args:
        """Отбираем имена по первой букве в цикле filter(lambda el: el[:1] == name[:1]"""
        my_dict.update({name[:1]: list(filter(lambda el: el[:1] == name[:1], args))})
    return my_dict


result = my_func('Марья', 'Иван', 'Света', 'Петя', 'Марсель', 'Павел', 'Илларион', 'Прошка', 'Сергей')
print(result)

# Отсортируем словарь по ключам. Воспользуемся встроенной функцией sorted()
# Полученный результат - новый объект Список. Обернем его обратно в словарь dict()
print('Отсортированный по ключам словарь')
print(dict(sorted(result.items())))

