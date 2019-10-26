import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

		ret, img = cap.read()
		img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		lower_red = np.array([0,50,50])
		upper_red = np.array([10, 255, 255])
		mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
		lower_red = np.array([170, 50, 50])
		upper_red = np.array([180, 255, 255])
		mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
		mask = mask0 + mask1
		output_img = img.copy()
		output_img[np.where(mask == 0)] = 0

		cv2.imshow("original", img)
		cv2.imshow("output", output_img)

		if (cv2.waitKey(1) & 0xFF == ord('q')):
				break


cv2.destroyAllWindows()				