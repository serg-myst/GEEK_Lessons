from sys import argv
from itertools import islice

'''
Вариант 2:
В этой задаче не сказано, что мы не должны читать весь файл. Говорится, что стоит об этом задуматься
Воспользуемся islice из библиотеки itertools
'''


def read_prices(arg):
    with open('bakery.csv','r',encoding='utf-8') as f:
        try:
            start = int(arg[1])-1
        except:
            start = None

        try:
            stop = int(arg[2])
        except:
            stop = None

        lines = islice(f, start, stop)
        for line in lines:
            print(line.replace('\n',''))


if __name__ == '__main__':
    read_prices(argv)