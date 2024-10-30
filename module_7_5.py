#--------------Файлы в операционной системе--------------

import os
from os import getcwd
import time


directory = '.'


for root, dirs, files in os.walk(directory):

    for file in files:
        filepath = os.path.join
        filetime = os.path.getmtime
        # time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize
        parent_dir = os.path.dirname
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: , Родительская директория: {parent_dir}')
