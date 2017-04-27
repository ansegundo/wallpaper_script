# pylint: skip-file

import os
import sys
import getpass
import ctypes
import easygui
from pathlib import Path
from random import randint

current_user = getpass.getuser()
default_path = os.path.join('c:/Users', current_user, 'pictures')

print(default_path)
wallpaper_list = []
SPI_SETDESKWALLPAPER = 20

msg = "Would you like to change the default folder?"+ "\n" +"C:\\Users\your_username\Pictures"
title = "Please Confirm"

if easygui.ccbox(msg, title):
    path = easygui.diropenbox()
else:
    path = default_path

try:
    os.chdir(path)
except TypeError:
    print('You did not choose a directory. Exiting now.')
    sys.exit(0)
        
print(path)

for item in Path('.').glob('*'):
    if item.is_file():
        print(item.absolute())
        wallpaper_list.append(str(item.absolute()))

set_wallpaper = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_list[randint(0,(len(wallpaper_list))-1)], 0)
if not set_wallpaper:
    print(ctypes.WinError())    
