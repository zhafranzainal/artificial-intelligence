import cv2
import numpy as np

img = cv2.imread("avenger.jpg")

# Change size based on scale
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Create a black mask with the same dimensions as the image
mask = np.zeros(img.shape[:2], dtype="uint8")

# Draw a white filled circle on the mask
cv2.circle(mask, (160, 200), 165, 255, -1)

# Apply the mask to the image using bitwise_and operation
img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
