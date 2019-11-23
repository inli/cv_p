#通过删除数据行/列压缩图片

import cv2 as cv
import numpy as np

img = cv.imread('D:\DELL\Pictures\865df19af3e24b67b9de00a39a2037f4.jpeg')

result = cv.imread('D:\DELL\Pictures\865df19af3e24b67b9de00a39a2037f4.jpeg',cv.IMREAD_REDUCED_COLOR_2)
#图像大小缩小1/2
    


cv.imshow('img',img)
cv.imshow('new',result)
cv.waitKey(0)
cv.destroyAllWindows()

