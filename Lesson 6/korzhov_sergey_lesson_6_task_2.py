import requests


def read_line(fl):
    for line in fl:
        yield line.split()[0]


def get_date():

    server_answer = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    if server_answer.status_code != 200:
        print(f'Ошибка получения запроса. Статус ответа: {server_answer.status_code}')

    answer_text = server_answer.text
    server_answer.close()

    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        f.writelines(answer_text)


get_date()

dct = {}  # Сделеам через словарь
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for ip in read_line(f):
        if dct.get(ip) is None:
            dct.update({ip: 1})
        else:
            dct.update({ip: dct.get(ip) + 1})
    num = 0
    ip = ''
    for key, item in dct.items():
        if item > num:
            num = item
            ip = key
    print(f'IP {ip} количество вызовов = {num}')
