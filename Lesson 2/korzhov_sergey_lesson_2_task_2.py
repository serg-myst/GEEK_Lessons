
list_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_words_for_print = [] #список для вывода на печать
for word in list_words:
    if word.isdigit():
        list_words_for_print.extend(['"#',word.zfill(2),'#"'])
    else:
        if word.startswith(('+','-')):
            list_words_for_print.extend(['"#', f'{word[:1]}'f'{word[1:].zfill(2)}', '#"'])
        else:
            list_words_for_print.append(word)
print(' '.join(list_words_for_print).replace('"# ','"').replace(' #"','"'))




