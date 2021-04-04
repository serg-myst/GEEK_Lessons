
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Основной вариант решения
tmp = set()
unique_numbers = set()

for num in src:
    if num not in tmp:
        unique_numbers.add(num)
    else:
        unique_numbers.discard(num)
    tmp.add(num)

unique_list = [num for num in src if num in unique_numbers]
print(unique_list)

# Еще вариант решения
# Пока не могу сказать работа через генератор таким образом это оптимизация?
tmp = set()  # Множество для последующей проверки вхождения
gen = (src[i] for i in range(len(src)) if not i == src.index(src[i]))  # Через генератор соберем повторяющиеся цифры
for num in gen:
    tmp.add(num)

unique_numbers = []
for num in src:
    if num not in tmp:
        unique_numbers.append(num)

print(unique_numbers)



