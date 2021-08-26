from json import dump, load
from os import walk, stat, path

size_file = {}
for root, dirs, files in walk('project'):
    for file in files:
        key_file = stat(path.join(root, file)).st_size // 10 * 10 + 10
        file_ext = file.rsplit('.')[-1]
        if key_file in size_file:
            size_file[key_file][1].append(file_ext)
            size_file[key_file] = (size_file[key_file][0] + 1, size_file[key_file][1])
        else:
            size_file.setdefault(key_file, (1, [file_ext]))

result = {k: size_file[k] for k in sorted(size_file.keys())}
with open('result.json', 'w') as f:
    dump(result, f)
with open('result.json', 'r') as f:
    print(load(f))
