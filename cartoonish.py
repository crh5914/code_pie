import numpy as np
import cv2
#1.使用canny边缘检测算法生成边缘图像
#2.将边缘图像与原图叠加
#3.将图像从RGB空间转换到HSI空间，同时增强S分量
origion_im = cv2.imread('origin.jpg')
edge_im = 255 - cv2.Canny(origion_im,150,200)
edge_im = cv2.cvtColor(edge_im,cv2.COLOR_GRAY2BGR)
fushion_im = cv2.bitwise_and(origion_im,edge_im)
fusion_im = cv2.cvtColor(fushion_im,cv2.COLOR_BGR2HSV)
fusion_im[:,:,1] = (fusion_im[:,:,1]+200)%256
fusion_im =  cv2.cvtColor(fushion_im,cv2.COLOR_HSV2BGR) 
cv2.imshow('fusion image',fushion_im)
cv2.waitKey(0)
cv2.destroyAllWindows()


