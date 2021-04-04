
numbers = int(input('Please, enter the number (>10):'))
nums_generator = (num for num in range(numbers+1) if num % 2 != 0)
print(*nums_generator,sep=',')
