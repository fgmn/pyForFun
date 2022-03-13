
import cv2
import math

def get_demo(img, label, out_width, out_height):
    out_radius = out_width if out_width < out_height else out_height
    small_img  = cv2.resize(img,   (out_width, out_height))
    small_label = cv2.resize(label, (out_width, out_height))
    for i in range(out_height):
        for j in range(out_width):
            distance = int(math.sqrt(i*i+j*j))
            # alpha = 1 if distance > out_radius else distance / out_radius
            alpha = 0.3
            for k in range(3):
                small_label[i][j][k] = int(alpha * small_img[i][j][k] + (1-alpha) * small_label[i][j][k])
    return small_label

img = cv2.imread('flag.jpg')
label = cv2.imread('cute.png')

pic = get_demo(img, label, 512, 512)
# print(pic)
cv2.imwrite('pic.png',pic)
cv2.imshow('pic', pic)
cv2.waitKey(0)