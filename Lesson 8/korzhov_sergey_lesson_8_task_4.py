
def val_checker(check):
    def wrapper(func):
        def check_values(*args):
            if check(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'wrong val: {args}')

        return check_values
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
print(calc_cube(-3))
