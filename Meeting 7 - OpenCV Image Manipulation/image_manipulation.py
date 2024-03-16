import cv2

img = cv2.imread("avenger.jpg")

print(img.shape)

# Change size based on dimension
# img = cv2.resize(img, (300, 400))

# Change size based on scale
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Apply a simple averaging filter to the image (uniform blur)
img_blurred = cv2.blur(img, (10, 10))

# Apply a box filter with more control over border handling and normalization
img_box_filtered = cv2.boxFilter(img, -1, (10, 10))

# Apply a Gaussian blur to the image
# Gaussian blur preserves edges better compared to simple averaging filters
img_gaussian_blurred = cv2.GaussianBlur(img, (9, 9), 1)

cv2.imshow("Resized Image", img)
cv2.imshow("Blurred Image", img_blurred)
cv2.imshow("Box Filtered Image", img_box_filtered)
cv2.imshow("Gaussian Blurred Image", img_gaussian_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
