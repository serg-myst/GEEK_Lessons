
percent = int(input('Введите процент: '))

str_percent = 'процент'

mas_excep = (1,2,3,4)

if percent >= 20:
    print('Внимание! Введенное число должно быть < 20')
else:
    if percent in mas_excep:
        if percent != 1:
            str_percent = str_percent + 'а'
    else:
        str_percent = str_percent + 'ов'

    print('{} {}'.format(percent,str_percent))

    #Выведем все склонения до 20
    print('================Проверка================')
    for percent in range(20):
        str_percent = 'процент'
        if percent in mas_excep:
            if percent != 1:
                str_percent = str_percent + 'а'
        else:
            str_percent = str_percent + 'ов'

        print('{} {}'.format(percent,str_percent))

