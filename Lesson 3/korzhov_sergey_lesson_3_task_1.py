
DICT_TRANSLATE = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(number):
    return DICT_TRANSLATE.get(number)


user_number = str(input('Please enter a number (one, two ...): '))
print(num_translate(user_number))


