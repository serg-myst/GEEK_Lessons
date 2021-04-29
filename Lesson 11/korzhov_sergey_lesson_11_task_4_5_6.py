from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class Warehouse:

    def __init__(self, warehouse_name, warehouse_type, code):
        # Реквизиты склада.
        self.warehouse_name = warehouse_name
        self.warehouse_type = warehouse_type
        self.__code = code
        self.__address = 'Москва, ул. Ленина 5'
        self.__rests = {}

    @property
    def code(self):
        return self.__code

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return f'Склад Код: {self.code}, Имя: {self.warehouse_name}, Тип: {self.warehouse_type}\n' \
               f'Адрес: {self.__address} \n' \
               f'Остатки на складе: {len(self.__rests.items())} шт. \n'

    def add_in_stock(self, unit):

        if type(unit) in (Printer, Scanner, Copier):
            if not self.__rests.get(unit.id, False):
                self.__rests[unit.id] = (datetime.now(), unit.equipment_type, unit)
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) принято на склад Код: {self.code}'
                    f' ({self.__address}).')
            else:
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) уже числится на складе Код:'
                    f' {self.code} {self.__address}).')

    def del_from_stock(self, unit):

        if type(unit) in (Printer, Scanner, Copier):
            if self.__rests.get(unit.id, '') != '':
                self.__rests.pop(unit.id)
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) списано со склада Код: {self.code}'
                    f' ({self.address}).')
            else:
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) не числится на складе Код: {self.code} '
                    f'({self.address}).')

    # Итератор для остатков на складе.
    def __iter__(self):
        return (el for el in self.__rests.items())


class Equipment(ABC):
    __types = {'p': 'Принтер', 's': 'Сканер', 'с': 'Ксерокс'}

    @abstractmethod
    def __init__(self, serial_number, eq_type):
        # Вся техника сначала приходит на главный склад.
        self.serial_number = serial_number
        self.__eq_type = self.__types.get(eq_type, 'Неизвестно')
        self.__id = uuid4()
        self.__price = 0

    @property
    def equipment_type(self):
        return self.__eq_type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'Обрудование ID: {self.__id}, Тип {self.equipment_type}, Серийный номер: {self.serial_number}, ' \
               f'Цена: {self.price} руб.\n'


class Printer(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 'p')
        self.__id = uuid4()
        self.__page_count = 10

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, value):
        self.__page_count = value

    def __str__(self):
        ret = super().__str__()
        return ret + f'Пробег: {self.page_count} стр. \n'


class Scanner(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 's')
        self.__id = uuid4()
        self.__dpi = 400

    @property
    def dpi(self):
        return self.__dpi

    @dpi.setter
    def dpi(self, value):
        dpis = [400, 600, 800, 1200]
        if value in dpis:
            self.__dpi = value
        else:
            self.__dpi = 400

    def __str__(self):
        ret = super().__str__()
        return ret + f'Разрешение сканирования: {self.dpi} dpi. \n'


class Copier(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 'c')
        self.__id = uuid4()


# Создадим два склада.
wh_main = Warehouse('Оптовый склад', 'Оптовый', '1')
wh_main.address = 'Москва, пр. Нефтяников ул.5 д.3'
wh_add = Warehouse('Розничный склад', 'Розничный', '2')
wh_add.address = 'Москва, Можайская ул. 10 д. 48'
# Создадим принтер
my_printer = Printer('E4544F1KNPRINT')
my_printer.price = 19900
my_printer.page_count = 45332
# Создадим сканер.
my_scanner = Scanner('E4544F1KZSCAN')
my_scanner.price = 16450
my_scanner.dpi = 800
# Покажем информацию о наших элементах.
print(wh_main)
print(wh_add)
print(my_printer)
print(my_scanner)

# Тестируем приходы и списания.
wh_main.add_in_stock(my_printer)
print(wh_main)
wh_main.del_from_stock(my_scanner)
wh_main.del_from_stock(my_printer)
wh_main.del_from_stock(my_printer)
# Проверим как можно перечислить остатки на складе.
# Оприходуем на запасной склад - пару единиц.
wh_add.add_in_stock(my_printer)
wh_add.add_in_stock(my_scanner)
# Ну и покажем их.
for el in wh_add:
    print('Элемент склада: ', el)
