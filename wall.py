# pylint: skip-file

import os
import sys
import getpass
import ctypes
import easygui
from pathlib import Path
from random import randint

current_user = getpass.getuser()
default_path = os.path.join('c:/Users', current_user, 'pictures/wallpaper')
print(default_path)
# wallpaper_path = easygui.diropenbox().replace('\\','\\\\')
wallpaper_list = []
SPI_SETDESKWALLPAPER = 20

path = easygui.diropenbox()
print(path)
os.chdir(path)
for item in Path('.').glob('*'):
    if item.is_file():
        print(item.absolute())
        wallpaper_list.append(str(item.absolute()))

set_wallpaper = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_list[randint(0,(len(wallpaper_list))-1)], 0)
if not set_wallpaper:
    print(ctypes.WinError())    

# print(wallpaper_list)
#count = len(path.files())
#print(count)
