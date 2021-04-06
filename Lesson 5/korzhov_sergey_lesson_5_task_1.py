

def nums_generator(n):
    for num in range(n + 1):
        if num % 2 != 0:
            yield num


numbers = int(input('Please, enter the number (>10):'))
gen_odd_numbers = nums_generator(numbers)

print(*gen_odd_numbers,sep=',')
