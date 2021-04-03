import requests
from datetime import date


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

    return print(f'{exchange_rates.get(curr.upper())}, {exchange_rates.get("date")}')


if __name__ == '__main__':

    currency_rates('usd')
    currency_rates('CAD')
    currency_rates('eur')
