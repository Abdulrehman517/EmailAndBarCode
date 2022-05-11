import cv2
img = cv2.imread('e.PNG')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img = 255 - grey_img
blurred = cv2.GaussianBlur(inverted_img, (21,21),0)
inverted_blur = 255 - blurred
pencil_sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)
cv2.imshow('original image', img)
cv2.imshow('pencil sketch',pencil_sketch)
# cv2.imshow('inverted', inverted_blur)
cv2.waitKey(0)