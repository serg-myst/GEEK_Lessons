from sys import argv

'''
В задании говорится, что надо выдавать сообщение об ошибке, если редактируемой строки нет
В данном контексте не знаю как это реализовать без чтения файла. Только, если заранее знать сколько строк в файле
'''

BYTES_IN_LINE = 12  # 10 - длина строки. 2 - символ перевода каретки (\n)


def get_line(rf, price_line):
    if price_line <= 0:
        return 0
    else:
        return price_line * BYTES_IN_LINE


def edit_price(line_number, price):
    with open("bakery.csv", 'r+', encoding='utf-8') as f:
        try:
            edit_line = get_line(f, line_number-1)  # Мы знаем, что первая строка у нас это всегда .tell() = 0
            f.seek(edit_line)
            for i in range(10 - len(price)):  # Здесь мы просто добиваем строку до нужной длины
                price += chr(0x20)
            f.write(price.replace('.',','))
        except:
            print('NoDataInFile')


if __name__ == '__main__':
    _script, line, edit_pr = argv
    edit_price(int(line), edit_pr)
