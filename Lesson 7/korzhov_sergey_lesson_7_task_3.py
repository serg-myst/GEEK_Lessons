import os
import shutil

FOLDER = r'my_project'
NEW_FOLDER = r'templates'

if not os.path.exists(NEW_FOLDER):
    os.mkdir(NEW_FOLDER)

DICT_COPY = {}


def show_dirs(dir_project):
    for file in os.scandir(dir_project):
        item_name = file.name
        if item_name.lower().endswith('.html'):
            new_path = os.path.join(NEW_FOLDER,os.path.join(dir_project.name,item_name))
            new_dir = os.path.join(NEW_FOLDER,dir_project.name)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            old_path = os.path.join(dir_project,item_name)
            DICT_COPY.update({old_path: new_path})
        if file.is_dir():
            show_dirs(file)
    return DICT_COPY


project_html = show_dirs(FOLDER)

for key, item in project_html.items():
    if not os.path.exists(item):
        shutil.copy(key, item)
