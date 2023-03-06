
import cv2
import numpy as np
import os

#cap = cv2.VideoCapture(0)
frame = cv2.imread('image.jpeg')

while(1):
	#_, frame = cap.read()
	# It converts the BGR color space of image to HSV color space
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# Threshold of blue in HSV space
	lower_blue = np.array([0, 0, 140])
	upper_blue = np.array([180, 255, 255])

	lower_green = np.array([0, 140, 0])
	upper_green = np.array([100, 255, 100])

	lower_white = np.array([200, 200, 200])
	upper_white = np.array([255, 255, 255])


	# preparing the mask to overlay
	maskb = cv2.inRange(hsv, lower_blue, upper_blue)
	
	maskg = cv2.inRange(hsv, lower_green, upper_green)

	maskw = cv2.inRange(hsv, lower_white, upper_white)
			
	# The black region in the mask has the value of 0,
	# so when multiplied with original image removes all non-blue regions
	resultb = cv2.bitwise_and(frame, frame, mask = maskb)

	resultg = cv2.bitwise_and(frame, frame, mask = maskg)
	
	resultw = cv2.bitwise_and(frame, frame, mask = maskw)

	cv2.imshow('frame', frame)
	cv2.imshow('maskb', maskb)
	cv2.imshow('result', resultb)
	
	cv2.imshow('maskg', maskg)
	cv2.imshow('result', resultg)
	
	cv2.imshow('maskw', maskw)
	cv2.imshow('result', resultw)
	
	cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
