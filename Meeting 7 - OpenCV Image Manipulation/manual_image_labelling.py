import cv2

img = cv2.imread("exercise.jpg")

height, width, channel = img.shape

cv2.rectangle(img, (300, 20), (450, 160), (0, 255, 0), 2)
img = cv2.putText(img, "Face", (300, 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

cv2.rectangle(img, (400, 260), (600, 390), (255, 0, 0), 2)
img = cv2.putText(img, "Laptop", (400, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

cv2.circle(img, (385, 380), 50, (0, 0, 255), 2)
img = cv2.putText(img, "Cup", (370, 320), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Labelled Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
