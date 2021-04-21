class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Пишем шариковой ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Пишем карандашом')


class Handle(Stationery):

    def draw(self):
        print('Пишем маркером')


s = Stationery()
s.draw()

p = Pen()
p.draw()

p1 = Pencil()
p1.draw()

h = Handle()
h.draw()
