duration = int(input('Введите промежуток времени, сек: '))

#86400 - секунд в дне, 3600 - секунд в часе, 60 - секунд в минуте, 1 - собственно секунда
list_time = (86400, 3600, 60, 1)
#для красивой печати
list_result = ('дн','час','мин','сек')

result = ''
for inx, value in enumerate(list_time):
    current_duration = duration // value
    if current_duration > 0:
        result = result + str(current_duration) + ' ' + list_result[inx] + ' '
    duration = duration - current_duration * value
print(result)