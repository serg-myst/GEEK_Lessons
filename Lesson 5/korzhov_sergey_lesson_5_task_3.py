
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Вася', 'Станислав'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = ((tutors[x],klasses[x]) if x < len(klasses) else (tutors[x],None) for x in range(len(tutors)))

print(gen)  # доказательство, что это генератор

# Вводим содержимое геператора пока он не истощится 'StopIteration'
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  # Здесь будет 'StopIteration'. Больше нет данных

'''
Еще вариант проверки вывод в цикле

for g in gen:
    print(g)
    
Второй раз этот цикл не сработает. На экране ничего не будет. Генератор пустой после первого прохода    

Для чего нужны генераторы? Для работы с большим количеством информации.
Например текстовые файлы большого размера, чтобы не загонять весь файл в память
'''

# print(*gen)  # вывод на печать всего содержимого генератора
