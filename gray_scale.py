from matplotlib import pyplot as plt
import cv2

img = cv2.imread('/Users/mustafa/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray)
plt.title('my picture')
plt.show()