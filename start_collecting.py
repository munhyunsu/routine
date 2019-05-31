import os
import pkgutil
import importlib


def get_files(path, ext='', recursive=False):
    """
    Read all files in path
    :param path: path for reading
    :return: absolute path of all files in directory list
    """
    path_list = [path]

    while len(path_list) > 0:
        cpath = path_list.pop()
        with os.scandir(cpath) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    if entry.name.endswith(ext):
                        yield entry.path
                    else:
                        if recursive:
                            path_list.append(entry.path)


collectors = list()
for name in get_files('./colls'):
    name = os.path.basename(name)[:-3]
    imported = importlib.import_module('colls'+'.'+name, name)
    class_name = name.split('_')[-1]
    class_object = getattr(imported, class_name)
    collectors.append(class_object())

for collector in collectors:
    collector.do_collect()

