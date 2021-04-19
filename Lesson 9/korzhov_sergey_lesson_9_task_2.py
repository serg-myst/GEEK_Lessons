class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, mass, thickness):
        result = (self._length * self._width * thickness * mass) / 1000
        return result


r = Road(5000, 20)
print(r.calculate(25,5))

r1 = Road(1000, 10)
print(r1.calculate(25,5))
