import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("D:/DELL/Pictures/test.png",cv.IMREAD_UNCHANGED)

plt.subplot(2,  1,  1)
plt.title('r,g,b')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])


plt.subplot(2,  1,  2) 
plt.title('gray')
plt.hist(img.ravel() , 256, [0, 256])

plt.show()
