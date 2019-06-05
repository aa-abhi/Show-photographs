import numpy as np
import cv2

img = cv2.imread("no.jpg",cv2.IMREAD_GRAYSCALE)


resized = cv2.resize(img,(400,400))
cv2.imshow("shapes", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#here you have to save the photographs first name as "a,b,c"

img1 = cv2.imread("a.png",cv2.IMREAD_GRAYSCALE)
resized = cv2.resize(img1,(400,400))
cv2.imshow("shapes", resized)
cv2.waitKey()
cv2.destroyAllWindows()

img1 = cv2.imread("b.png",cv2.IMREAD_GRAYSCALE)
resized = cv2.resize(img1,(400,400))
cv2.imshow("shapes", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = cv2.imread("c.jpg",cv2.IMREAD_GRAYSCALE)
resized = cv2.resize(img1,(400,400))
cv2.imshow("shapes", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



