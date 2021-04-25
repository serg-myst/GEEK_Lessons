class Cell:

    def __init__(self, c):
        if not isinstance(c, int):
            raise ValueError('Numbers of cells must be "int"')
        self.c = c

    def __str__(self):
        return f'Клетка {self.c}'

    def __add__(self, other):
        return Cell(self.c + other.c)

    def __sub__(self, other):
        if other.c < self.c:
            return Cell(self.c - other.c)
        raise ValueError('Numbers of cell 2 must be < cell 1')

    def __mul__(self, other):
        return Cell(self.c * other.c)

    def __floordiv__(self, other):
        return Cell(self.c // other.c)

    def make_order(self, n):
        s = ''
        for i in range(self.c):
            s += '*'
            if (i + 1) % 5 == 0 and (i + 1) != self.c:
                s += r'\n'
        return s


# Сложение
c1 = Cell(3)
c2 = Cell(5)
print(c1 + c2)

'''
# Вычитание (ошибка)
c1 = Cell(2)
c2 = Cell(3)
print(c1 - c2)
'''
# Вычитание
c1 = Cell(8)
c2 = Cell(3)
print(c1 - c2)

# Умножение
c1 = Cell(2)
c2 = Cell(2)
print(c1 * c2)

# Деление
c1 = Cell(8)
c2 = Cell(3)
print(c1 // c2)

# Ряды
c = Cell(17)
print(c.make_order(5))
