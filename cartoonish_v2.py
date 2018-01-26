import cv2
import os

def cartoonlize(image):
	num_down = 1
	num_filter = 2
	for _ in range(num_down):
		image = cv2.pyrDown(image)
	print('after pyrdown, image shape:{}'.format(image.shape))
	for _ in range(num_filter):
		image = cv2.bilateralFilter(image,d=9,sigmaColor=2,sigmaSpace=2)
	print('after bilateralfilter,image shape:{}'.format(image.shape))
	for _ in range(num_down):
		image = cv2.pyrUp(image)
	#print('after pyrup, image shape:{}'.format(image.shape))
	new_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	new_image = cv2.medianBlur(new_image,7)
	print(image.shape)
	edge_image = cv2.adaptiveThreshold(new_image, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)
	edge_image = cv2.cvtColor(edge_image,cv2.COLOR_GRAY2RGB)
	print('edge_image shape:{}'.format(edge_image.shape))
	image = cv2.bitwise_and(image,edge_image)
	print('after all opertation, image shape:{}'.format(image.shape))
	return image

img = cv2.imread('origin.jpg')
cv2.imshow('origin image',img)
img = cartoonlize(img)
cv2.imshow('cartoonlize image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()