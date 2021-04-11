from sys import argv

'''
Вариант 1:
В этой задаче не сказано, что мы не должны читать весь файл. Говорится, что стоит об этом задуматься
Сделаем через список и по срезу найдем, что требуется
'''


def read_prices(arg):
    with open('bakery.csv','r',encoding='utf-8') as f:
        prices = list((el.replace('\n', '') for el in f.readlines()))

        if len(arg) == 1:
            for price in prices:
                print(price)
        else:
            if len(arg) == 2:
                for price in prices[int(arg[1])-1:]:
                    print(price)
            else:
                for price in prices[int(arg[1])-1:int(arg[2])]:
                    print(price)


if __name__ == '__main__':
    read_prices(argv)
