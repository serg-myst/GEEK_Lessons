import requests


def read_line(f):
    for line in f:
        yield line.replace('"','').split()


def get_date():

    server_answer = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    if server_answer.status_code != 200:
        print(f'Ошибка получения запроса. Статус ответа: {server_answer.status_code}')

    answer_text = server_answer.text
    server_answer.close()

    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        f.writelines(answer_text)


get_date()

log = []
with open('nginx_logs.txt','r',encoding='utf-8') as f:
    for line in read_line(f):
        (a, b, c) = line[0], line[5], line[6]
        log.append((a, b, c))
    print(log)