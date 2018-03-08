import cv2
import numpy as np
import matplotlib.pyplot as plt

imageName = input("Enter the image input: ")
imageFormat = "."+input("Enter the image extension: ")

img = cv2.imread(imageName+imageFormat)

#img_gray = cv2.GaussianBlur(img, (5, 5), 0)
roi = img[:25,:25]
print(roi)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 25, 1)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                           kernel, iterations=4)

cont_img = closing.copy()

_, contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
									   cv2.CHAIN_APPROX_SIMPLE)
       
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 4000 or area > 8000:
        continue

        if len(cnt) < 5:
            continue

        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(roi, ellipse, (0,255,0), 2)

cv2.imshow("Morfologico", closing)
cv2.imshow("Umbral Adaptivo", thresh)
cv2.imshow('Contonrnos', roi)

#cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

###
#img = cv2.resize(img, (640, 480))

#mp_img = mpimg.imread('coins.jpg')
#print(mp_img)

#cv2.imshow("Coins", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


def recogniseCoins():
	return