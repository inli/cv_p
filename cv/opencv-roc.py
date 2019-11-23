import numpy as np
from matplotlib import pyplot as plt
from scipy import io



f = open("D:/DELL/Documents/ViolaJonesScore_n0_ContROC.txt",'r')

x = []
y = []

for line in f.readlines():                          #依次读取每行  
    line = line.strip()                             #去掉每行头尾空白  
    xy = line.split(' ',1)
    #print(xy)
    x.append(float(xy[1]))
    y.append(float(xy[0]))
 
# 关闭文件
f.close()

plt.title("OPENCV-FACEDETECT-ROC")
plt.ylabel('true positive rate')
plt.xlabel('false positive')
plt.autoscale()
plt.plot(x,y)

plt.show()

