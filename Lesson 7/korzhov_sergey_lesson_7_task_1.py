import os

parent_dir = 'my_project'
directories = ['settings','mainapp','adminapp','authapp']

for dir in directories:
    path = os.path.join(parent_dir,dir)
    os.makedirs(path,exist_ok = True)  # Не создает директорию, если уже существует