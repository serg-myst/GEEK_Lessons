import requests

'''currency_rates()

Функция получает курсы валют с указанного сайта
Т.к парсить xml в задании не разрешается, то будем разбираться со строкой. xml - упорядоченная структура
Возьмем нужные нам тэги в '#-' и '-#'. Составим 2 списка с наименования валют и их курсами
После обработки функция вернет нам словарь, который мы передадим в функцию для получения курса currency_rates()

'''


def currency_rates(curr):

    exchange_rates = {}

    server_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if server_answer.status_code != 200:
        print(f'Ошибка получения запроса. Статус ответа: {server_answer.status_code}')
        return exchange_rates

    answer_text = server_answer.text

    server_answer.close()

    answer_text_currency = answer_text.replace('<CharCode>', '#-').replace('</CharCode>', '-#').split('#')
    currency_list = list(filter(lambda el: el[:1] == '-', answer_text_currency))

    answer_text_rates = answer_text.replace('<Value>', '#-').replace('</Value>', '-#').split('#')
    currency_values_list = list(filter(lambda el: el[:1] == '-', answer_text_rates))

    # Заполним словарь корректными значениями
    for index, value in enumerate(currency_list):
        current_rate = float(currency_values_list[index].replace('-', '').replace(',', '.'))
        exchange_rates.update({value.replace('-', ''): current_rate})

    return exchange_rates.get(curr.upper())


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('asd'))
