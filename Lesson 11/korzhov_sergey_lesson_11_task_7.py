class ComplexNum:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        delimiter = '+'
        if self.img < 0:
            delimiter = ''
        return f'({self.real}{delimiter}{self.img}j)'

    # Складываем отдельно реальную часть и мнимую часть
    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.img + other.img)

    # (a1+b1J) * (a2+b2j) = a1*a2 + a1*b2j + b1j*a2 + b1j*b2j. Последнее j**2 = -1
    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.img * other.img,
                          self.real * other.img + self.img * other.real)


print('Собственный класс сложение')
a = ComplexNum(-1, 1)
b = ComplexNum(-2, -7)
print(a + b)

# Проверим встроенным методом
print('Встроенный класс сложение')
a = complex(-1, 1)
b = complex(-2, -7)
print(a + b)

print('Собственный класс умножение')
a = ComplexNum(5, -3)
b = ComplexNum(2, 7)
print(a * b)

# Проверим встроенным методом
print('Встроенный класс умножение')
a = complex(5, -3)
b = complex(2, 7)
print(a * b)