# -*- coding: utf-8 -*-
import subprocess
import shutil

caminho_atual=subprocess.os.getcwd()


for f in subprocess.os.listdir(caminho_atual):
    filename, file_ext = subprocess.os.path.splitext(f)

    try:
        if not file_ext:
            pass
        elif file_ext in ('.jpg','.png','gif','jpeg'):
            shutil.move(subprocess.os.path.join(caminho_atual, f'{filename}{file_ext}'),subprocess.os.path.join(caminho_atual, 'testeMove', f'{filename}{file_ext}'))


    except (FileNotFoundError, PermissionError):
        print('sem permissão')
        pass
