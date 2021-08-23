from itertools import zip_longest
from json import dump

with open('user.csv', 'r') as user, open('hobby.csv', 'r') as hobby:
    user = user.read().splitlines()
    hobby = hobby.read().splitlines()
if len(user) >= len(hobby):
    fin_list = dict(zip_longest(user, hobby, fillvalue=None))
    with open('fin_dict.txt', 'w') as f:
        dump(fin_list, f, ensure_ascii=False)
else:
    exit(1)
