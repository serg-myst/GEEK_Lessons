import requests
from datetime import date

'''get_exchange_rates_values()

Функция получает курсы валют с указанного сайта
Т.к парсить xml в задании не разрешается, то будем разбираться со строкой. xml - упорядоченная структура
Возьмем нужные нам тэги в '#-' и '-#'. Составим 2 списка с наименования валют и их курсами
После обработки функция вернет нам словарь, который мы передадим в функцию для получения курса currency_rates()
Добавим еще и дату курса

'''


def currency_rates(curr):

    exchange_rates = {}

    server_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if server_answer.status_code != 200:
        print(f'Ошибка получения запроса. Статус ответа: {server_answer.status_code}')
        return exchange_rates

    answer_text = server_answer.text

    server_answer.close()

    # Где дата мы знаем, пока формат не поменяют
    date_str = '<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="'
    rates_date_list = answer_text.replace(date_str, '')[:10].split('.')

    # По условию надо получить тип 'Date'
    rates_date = date(int(rates_date_list[2]),int(rates_date_list[1]),int(rates_date_list[0]))

    exchange_rates.update({'date': rates_date})

    answer_text_currency = answer_text.replace('<CharCode>', '#-').replace('</CharCode>', '-#').split('#')
    currency_list = list(filter(lambda el: el[:1] == '-', answer_text_currency))

    answer_text_rates = answer_text.replace('<Value>', '#-').replace('</Value>', '-#').split('#')
    currency_values_list = list(filter(lambda el: el[:1] == '-', answer_text_rates))

    # Заполним словарь корректными значениями
    for index, value in enumerate(currency_list):
        current_rate = float(currency_values_list[index].replace('-', '').replace(',', '.'))
        exchange_rates.update({value.replace('-', ''): current_rate})

    return exchange_rates.get('date'), exchange_rates.get(curr.upper())


date_rates, rate = currency_rates('usd')
print(f'{rate}, {date_rates}')
date_rates, rate = currency_rates('EUR')
print(f'{rate}, {date_rates}')