from sys import argv

'''
Работаем с файлом, как с полями таблицы базы данных. Заранее позаботимся о длине строки
Это нам пригодится в последнем задании для редактирования суммы
Без этой манипуляции будет проблематично искать нужные строки без чтения файла
'''


def write_price(str_price):
    with open('bakery.csv','a',encoding='utf-8') as f:
        for x in range(10 - len(str_price)):  # Делаем строку длиной 10 символов, чтобы наши строки были одной длины
            str_price += chr(0x20)
        f.write(f'{str_price.replace(".",",")}\n')


if __name__ == '__main__':
    _script, price = argv
    write_price(str(float(price)))  # Передаем число формата 125.14, 145 и т.д. Обработку ошибок ввода не ставил
