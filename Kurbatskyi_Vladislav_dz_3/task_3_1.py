nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate():
    numbers = input()
    print(nums.get(numbers.lower()))


# num_translate()


def num_translate_adv():
    numbers = input()
    if numbers.istitle():
        print(nums.get(numbers.lower()).title())
    else:
        print(nums.get(numbers.lower()))


num_translate_adv()


""" from translate import Translator
translator = Translator(from_lang='en', to_lang='ru')
text = str(input())
tr_text = translator.translate(text)
print(tr_text)"""
