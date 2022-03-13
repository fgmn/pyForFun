

import cv2
import numpy as np


p1 = cv2.imread('flag.jpg')     # 返回类型： <class 'numpy.ndarray'>
p2 = cv2.imread('cute.png')

# print(p1)
# print(p2)
print(type(p1))
# print('\n')

img1 = cv2.resize(p1, (512, 512)) #国旗图片
img2 = cv2.resize(p2, (512, 512)) #微信头像


middle = 512    #渐变截至位置(0-512)

mask1 = np.repeat(np.tile(np.linspace(0, 1, middle), (img1.shape[1], 1))[:, :, np.newaxis], 3, axis=2)
mask2 = np.repeat(np.tile(np.linspace(1, 0, middle), (img1.shape[1], 1))[:, :, np.newaxis], 3, axis=2)

# print(mask1)
# print('\n')

# numpy.zeros(shape，dtype=float，order = 'C')
ones = np.ones((512, 512-middle, 3))
zero = np.zeros((512, 512-middle, 3))

# print(ones)
# print('\n')
# print(zero)

mask1 = np.concatenate((mask1, zero), axis=1)
mask2 = np.concatenate((mask2, ones), axis=1)

final = np.uint8(img1 * mask1 + img2 * mask2)

# cv2.imwrite('final.png', final)
# cv2.imshow('final', final)
# cv2.waitKey(0)