import random


def get_jokes(n, rep_words=False):
    """
    n - number of jokes
    rep_words - use repetitions. Default no
    """

    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

    list_len = min(len(nouns),len(adverbs),len(adjectives))
    result = []
    for j in range(min(n,list_len)):
        nouns_rand = random.randint(0,list_len - 1)
        adverbs_rand = random.randint(0, list_len - 1)
        adjectives_rand = random.randint(0, list_len - 1)
        result.append(f'{nouns[nouns_rand]} {adverbs[adverbs_rand]} {adjectives[adjectives_rand]}')

        if not rep_words:
            nouns.pop(nouns_rand)
            adverbs.pop(adverbs_rand)
            adjectives.pop(adjectives_rand)
            list_len -= 1

    return result


user_choice = str(input('Do you want to use repetitions in jokes (y/n): '))
num_jokes = int(input('Please enter the number of jokes: '))

if user_choice in ('y', 'Y'):
    jokes = get_jokes(num_jokes,True)
else:
    jokes = get_jokes(num_jokes)

print(jokes)

# Добавил именованный аргумент rep_words (повторять слова в шутках). По умолчанию нет (False).
# Если пользователь говорит 'y', то передаем в функцию True (разрешаем повторы)