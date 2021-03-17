result_a = 0
result_b = 0
mas_3 = []
#Заполняем массив нечетных чисел возведенных в куб
for number in range(1,1001,2):
    mas_3.append(number ** 3)

#Обходим массив и проверяем по условия Задания a и сразу Задание b
for i in range(len(mas_3)):
    current_number_a = mas_3[i]
    current_number_b = current_number_a + 17
    current_sum_a = 0
    current_sum_b = 0
    while current_number_a != 0:
        current_sum_a = current_sum_a + current_number_a % 10
        current_number_a = current_number_a // 10
    while current_number_b != 0:
        current_sum_b = current_sum_b + current_number_b % 10
        current_number_b = current_number_b // 10

    if current_sum_a % 7 == 0:
        result_a = result_a + mas_3[i]
    if current_sum_b % 7 == 0:
        result_b = result_b + (mas_3[i] + 17)


print('Результат по заданию a = {}'.format(result_a))
print('Результат по заданию b = {}'.format(result_b))