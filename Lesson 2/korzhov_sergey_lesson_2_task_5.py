
#Скорее всего, я забежал вперед. Все циклы внутри join можно вынести и создать отдельный список внутри цикла. Посмотрел по справочнику, что так делать можно.

prices = [1548,15.45,12.16,45.15,78.1,589,4.2,65.36,450,78.3]

#Задание a. Вывоим в одну строку ##руб ##коп
print('Задание a. Выводим цены в одну строку=======================================================')
print(', '.join(['{} руб {} коп'.format(int(price),f'{price:.2f}'[-2:]) for price in prices]))

#Задание b. Сортируем цены по возрастанию. В подзадаче не сказано, что формат цен должен быть (##руб ##коп). Не проблема, вместо str(price) пишем, как в подзадаче выше
print()
print('Задание b. Сортируем по возврастанию (докажем, что наш объект остался прежним)============')
print('id до сортировки: {}'.format(id(prices)))
prices.sort()
print(', '.join([str(price) for price in prices]))
print('id после сортировки: {}'.format(id(prices)))

#Задание с. Создадим новый список. В ТЗ не сказано, что надо что-то доказать, но покажем, что наш новый список - это новый объект. В ТЗ не сказано, что надо выводить цены, поэтому покажем сам список
print()
print('Задание c. Создаем новый список по убываению (докажем, что наш объект новый)===============')
print('id до сортировки: {}'.format(id(prices)))
prices_sorted = sorted(prices, reverse=True)
print(prices_sorted)
print('id после сортировки: {}'.format(id(prices_sorted)))

#Задание d. Выводим цены самых дорогих товаров, но по возврастанию цены. Опять же формат цен. Не сказано, что должны быть ##руб ##коп. Не проблема, вместо str(price) пишем, как в первой подзадаче
print()
print('Задание d. Выводим первые 5 дорогих товаров, но в порядке возрастания цены==================')
print(', '.join([str(price) for price in prices_sorted[:5][::-1]]))