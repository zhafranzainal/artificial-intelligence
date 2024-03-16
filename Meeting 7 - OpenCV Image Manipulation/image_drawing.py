import cv2

img = cv2.imread("avenger.jpg")

# Change size based on scale
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

height, width, channel = img.shape

# Draw a green line from top-left to bottom-right
cv2.line(img, (0, 0), (width, height), (0, 255, 0), 6)
# Draw a yellow line from top-right to bottom-left
cv2.line(img, (width, 0), (0, height), (55, 200, 255), 3)

# Draw a filled green rectangle at the top
cv2.rectangle(img, (0, 0), (width, 100), (0, 255, 0), -1)
# Draw a blue rectangle with a border at the bottom
cv2.rectangle(img, (0, 300), (width, height), (255, 0, 0), 5)

# Draw a red filled circle at (100, 100) with a radius of 40
cv2.circle(img, (100, 100), 40, (0, 0, 255), -1)
# Draw a white filled circle inside the previous one
cv2.circle(img, (100, 100), 20, (255, 255, 255), -1)

# Draw a red filled circle at (250, 100) with a radius of 40
cv2.circle(img, (250, 100), 40, (0, 0, 255), -1)
# Draw a white filled circle inside the previous one
cv2.circle(img, (250, 100), 20, (255, 255, 255), -1)

# Add red "Avenger" text at (100, 40)
img = cv2.putText(img, "Avenger", (100, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
# Add white "OpenCV" text at the bottom
img = cv2.putText(img, "OpenCV", (100, height - 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
