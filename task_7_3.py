from os import walk, makedirs, path

start_dir = 'project'
fin_dir = 'templates'

for root, _, _ in walk(start_dir):
    makedirs(path.join(fin_dir, path.relpath(root, start_dir)), exist_ok=True)
