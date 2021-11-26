import os
from os import listdir
from os.path import isfile, join
import cv2


if __name__ == '__main__':
    input_dir = './inputs/'
    base_output = './results'
    files = [f for f in listdir(input_dir)]
    print(files)
    for file in files:
        file_path = f'{input_dir}/{file}'

        # Read the image
        img = cv2.imread(file_path)
        print(img.shape)
        height = img.shape[0]
        width = img.shape[1]

        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]

        cv2.imwrite(f'{base_output}/{file}', s1)
        # cv2.imwrite('./results/two.png', s2)
