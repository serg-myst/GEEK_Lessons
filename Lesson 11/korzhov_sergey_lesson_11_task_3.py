class Error(Exception):
    pass


inp_data = ''
my_list = []
while inp_data != 'stop':
    inp_data = input("Введите число (наберите 'stop', чтобы завершить ввод): ")
    try:
        if inp_data == 'stop':
            break
        elif inp_data.startswith('-'):  # Отработаем отрицательные числа
            if not inp_data[1:].isdigit():
                raise Error
        elif not inp_data.isdigit():
            raise Error
    except Error:
        print('Ошибка. Введите число')
    else:
        my_list.append(int(inp_data))

print(my_list)