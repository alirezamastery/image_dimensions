import os
from os import listdir
from os.path import isfile, join
import shutil
from PIL import Image
from pathlib import Path


wallpaper_dir = 'F:/pics/wallpapers/Nebula'
base_output = 'C:/Users/ALIREZA/PycharmProjects/wallpaper/wallpapers'
files = [f for f in listdir(wallpaper_dir) if isfile(join(wallpaper_dir, f))]
print(files)
for file in files:
    file_path = f'{wallpaper_dir}/{file}'
    with Image.open(file_path) as img:
        print(file)
        w, h = img.size
        output = f'{base_output}/{w}_{h}_{file}'
        shutil.copy2(file_path, output)
