from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    joke = []
    for i in range(n):
        joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    print(joke)


get_jokes(5)
