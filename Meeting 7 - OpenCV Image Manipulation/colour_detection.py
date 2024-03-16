import cv2
import numpy as np

img = cv2.imread("avenger.jpg")

# Change size based on scale
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

height, width, channel = img.shape

# Draw lines
cv2.line(img, (0, 0), (width, height), (0, 255, 0), 6)
cv2.line(img, (width, 0), (0, height), (55, 200, 255), 3)

# Draw rectangles
cv2.rectangle(img, (0, 0), (width, 100), (0, 255, 0), -1)
cv2.rectangle(img, (0, 300), (width, height), (255, 0, 0), 5)

# Draw circles
cv2.circle(img, (100, 100), 40, (0, 0, 255), -1)
cv2.circle(img, (100, 100), 20, (255, 255, 255), -1)
cv2.circle(img, (250, 100), 40, (0, 0, 255), -1)
cv2.circle(img, (250, 100), 20, (255, 255, 255), -1)

# Add texts
img = cv2.putText(img, "Avenger", (100, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
img = cv2.putText(img, "OpenCV", (100, height - 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

# Define colour ranges with lower and upper bounds
red = ([0, 0, 30], [50, 56, 255])
blue = ([30, 0, 0], [255, 150, 50])
green = ([0, 30, 0], [100, 255, 100])
white = ([255, 255, 255], [255, 255, 255])

# Create a list of colour ranges
boundaries = [red, blue, green, white]

for (lower, upper) in boundaries:
    # Convert the lower and upper bounds to NumPy arrays
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # Create a mask using the lower and upper bounds
    mask = cv2.inRange(img, lower, upper)

    # Apply the mask to the image using bitwise AND operation
    output = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Colour Detection", output)
    cv2.waitKey(0)

cv2.destroyAllWindows()
