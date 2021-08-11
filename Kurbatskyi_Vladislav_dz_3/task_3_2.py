def thesaurus(*args):
    name = list(sorted(map(str, args)))
    names = {}
    for n in name:
        first_letter = n[0]
        names[first_letter] = names.get(first_letter, []) + [n]
    print(names)


thesaurus("Иван", "Мария", "Петр", "Илья")
