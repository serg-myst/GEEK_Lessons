"""
Для примера добавил в функцию несколько позиционных аргументов, чтобы показать как будет выглядеть в логировании
Для логирования именованных аргументов работаем через *kwargs
"""


def type_logger(func):
    def wrapper(*args):
        res = func(*args)
        print(f'{func.__name__}({", ".join(f"{str(ar)}: {type(ar)}" for ar in args)})')
        return res

    return wrapper


@type_logger
def calc_cube(x, y, z):
    return x ** 3 - y + z


result = calc_cube(5, 6, 8)
print(result)
