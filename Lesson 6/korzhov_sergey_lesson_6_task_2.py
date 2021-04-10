
def read_line(fl):
    for line in fl:
        yield line.split()[0]


dct = {}  # Сделеам через словарь
with open('parse.txt', 'r', encoding='utf-8') as f:
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
