from os import makedirs, path, curdir

project_path = 'project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in paths:
    makedirs(path.join(curdir, project_path, i), exist_ok=True)
