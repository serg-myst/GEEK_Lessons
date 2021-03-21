#Новый список не создаем
#Просто добавим в конец существующего списка нужные элементы. В контексте данной задачи почему нет...
#А для вывода на печать сделаем срез

list_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_length = len(list_words)
for i in range(list_length):
    word = list_words[i]
    if word.isdigit():
        list_words.extend(['"#',word.zfill(2),'#"'])
    else:
        if word.startswith(('+','-')):
            list_words.extend(['"#', f'{word[:1]}'f'{word[1:].zfill(2)}', '#"'])
        else:
            list_words.append(word)
print(' '.join(list_words[list_length:]).replace('"# ','"').replace(' #"','"'))