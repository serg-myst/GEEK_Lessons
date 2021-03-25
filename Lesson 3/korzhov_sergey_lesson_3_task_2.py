
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


def num_translate_adv(number):
    word = DICT_TRANSLATE.get(number.lower())
    if word is None or not number.istitle():
        return word
    return word.title()


user_number = str(input('Please enter a number ((O)one, (T)two ...): '))
print(num_translate_adv(user_number))