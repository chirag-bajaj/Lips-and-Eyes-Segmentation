import os
import cv2
import glob
import numpy as np
from utils import make_folder

label_list = ['l_eye', 'r_eye', 'u_lip', 'l_lip']

folder_base = 'CelebAMaskHQ-mask-anno'
folder_save = 'CelebAMaskHQ-mask'

img_num = 700

make_folder(folder_save)

for k in range(img_num):
	folder_num = k // 2000
	im_base = np.zeros((1024, 1024))
	for idx, label in enumerate(label_list):
		filename = os.path.join(folder_base, str(folder_num), str(k).rjust(5, '0') + '_' + label + '.png')
		if (os.path.exists(filename)):
			print (label, idx+1)
			im=cv2.imread(filename)
			im = im[:, :, 0]
			im_base[im != 0] = 255
	
	filename_save = os.path.join(folder_save, str(k) + '.png')
	print (filename_save)
	cv2.imwrite(filename_save, im_base)

