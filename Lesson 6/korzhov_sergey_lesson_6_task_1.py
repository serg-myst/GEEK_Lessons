
def read_line(f):
    for line in f:
        yield line.replace('"','').split()


log = []
with open('parse.txt','r',encoding='utf-8') as f:
    for line in read_line(f):
        (a, b, c) = line[0], line[5], line[6]
        log.append((a, b, c))
    print(log)