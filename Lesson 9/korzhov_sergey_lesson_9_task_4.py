class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        print(f'Машина повернула {direction}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class SportCar(Car):

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


t = TownCar()
t.speed = 65
t.name = 'Dodge'
t.color = 'Зеленый'
print(f'Автомобиль {t.name} цвет {t.color} движется со скорость {t.speed}')
t.go()
t.show_speed()
t.turn('направо')
t.stop()

w = WorkCar()
w.speed = 35
w.name = 'Man'
w.color = 'Красный'
print(f'Автомобиль {w.name} цвет {w.color} движется со скорость {w.speed}')
w.go()
w.show_speed()
w.turn('налево')
w.stop()

p = PoliceCar()
p.speed = 0
p.name = 'Skoda'
p.color = 'сине-белый'
p.is_police = True
print(f'Автомобиль {p.name} цвет {p.color} движется со скорость {p.speed}')
print(f'Автомобиль полиции {p.is_police}')
p.stop()
p.show_speed()

