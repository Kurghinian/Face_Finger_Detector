import cv2
import numpy

image = cv2.imread('balloon.jpg')
cv2.putText(image, "ջվգե", ( 200, 100), 0, 3, (255, 255,255), 5)
cv2.imshow("image",image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
