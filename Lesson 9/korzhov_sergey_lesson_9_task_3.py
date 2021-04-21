class Worker:
    name = 'Петр'
    surname = 'Петров'
    position = 'Слесарь'

    def __init__(self, _income):
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        return ''.join(f'{self.name} {self.surname}')

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


p = Position({"wage": 1000, "bonus": 3000})
p.name = 'Иван'
p.surname = 'Иванов'
p.position = 'Дворник'
print(p.get_full_name())
print(p.get_total_income())

p = Position({"wage": 5000, "bonus": 1000})
p.name = 'Сидр'
p.surname = 'Сидоров'
p.position = 'Кочегар'
print(p.get_full_name())
print(p.get_total_income())
