import cv2
import numpy as np
import os

in0 =input("Enter Image Name:-\n:")
in1 =input("Enter Image Type:-\n:")
nam = in0 + "." + in1

frame = cv2.imread(nam)

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

cv2.imshow('Input', frame)

cv2.imshow('OutputB', maskb)
#cv2.imshow('resultb', resultb)

cv2.imshow('OutputG', maskg)
#cv2.imshow('resultg', resultg)

cv2.imshow('OutputW', maskw)
#cv2.imshow('resultw', resultw)
masked_Area = np.sum(frame)
masked_areaB = np.sum(maskb == 255)
masked_areaG = np.sum(maskb == 0)

print(masked_areaB)
print(masked_areaG)
print(masked_areaB + masked_areaG)
print(masked_Area)

#filename1 = 'result image.jpg'
#filename2 = 'savedImage2.jpg'
#filename3 = 'savedImage3.jpg'

#cv2.imwrite(filename1, resultb) 
#cv2.imwrite(filename2, resultg) 
#cv2.imwrite(filename3, resultw) 

cv2.waitKey(0)

cv2.destroyAllWindows()
#cap.release()

