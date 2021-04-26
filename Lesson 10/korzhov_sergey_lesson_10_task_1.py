class Matrix:
    def __init__(self, param):
        # Проверим на соответствие матрице
        error = 'Переданный параметр не является матрицей'
        if not isinstance(param, list):
            raise ValueError(error)
        else:
            if len(param) < 2:
                raise ValueError(error)
            else:
                l = len(param[0])
                for i in param:
                    if len(i) != l:
                        raise ValueError(error)
                    l = len(i)
        self.param = param

    def __str__(self):
        s = ''
        for i in self.param:
            for j in i:
                s += ' ' + str(j)
            s += '\n'
        return s

    def __add__(self, other):
        m = []
        for index, value in enumerate(self.param):
            m1 = []
            for index1, value1 in enumerate(self.param[index]):
                m1.append(value1 + other.param[index][index1])
            m.append(m1)
        return Matrix(m)


mc1 = Matrix([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
print(mc1)
mc2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
print(mc2)
print(mc1 + mc2)
