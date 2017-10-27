import numpy as np
import cv2

def preprocess(img):
	cv2.imshow("Input",img)
	imgBlurred = cv2.GaussianBlur(img, (5,5), 0)
	gray = cv2.cvtColor(imgBlurred, cv2.COLOR_BGR2GRAY)
	sobelx = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=3)
	ret2,threshold_img = cv2.threshold(sobelx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	cv2.imshow("Threshold",threshold_img)
	return threshold_img

def extract_contours(threshold_img):
	element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(17, 3))
	morph_img_threshold = threshold_img.copy()
	cv2.morphologyEx(src=threshold_img, op=cv2.MORPH_CLOSE, kernel=element, dst=morph_img_threshold)
	cv2.imshow("Morphed",morph_img_threshold)
	cv2.waitKey(0)

	im2,contours, hierarchy= cv2.findContours(morph_img_threshold,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
	return contours

def isMaxWhite(plate):
	avg = np.mean(plate).astype(uint8)
	if(avg>=100):
		return True
	else:
 		return False

def validate(rect):
	print("TODO!")

def func(img,contours):
	for i,cnt in enumerate(contours):
		min_rect = cv2.minAreaRect(cnt)



if __name__ == '__main__':
	print "START"
	img = cv2.imread("test.jpeg")
	threshold_img = preprocess(img)
	contours= extract_contours(threshold_img)

	# if len(contours)!=0:
	# 	print len(contours) #Test
	# 	cv2.drawContours(img, contours, -1, (0,255,0), 1)
	# 	cv2.imshow("Contours",img)
	# 	cv2.waitKey(0)

	func(img,contours)
