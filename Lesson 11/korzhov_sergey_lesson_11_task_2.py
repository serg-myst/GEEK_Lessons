class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise OwnError("Введите число отличное от 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Делим 15 на {inp_data} = {15 / inp_data}")
