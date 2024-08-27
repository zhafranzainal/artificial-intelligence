import cv2
import imutils
import numpy as np
import easyocr

# Load and process the image
img = cv2.imread('images/1.jpg')
imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the gray image before displaying
scale_factor = 0.5

imgGrayScaleResized = cv2.resize(imgGrayScale, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
cv2.imshow("Image", imgGrayScaleResized)

# Apply filters and find edges
bfilter = cv2.bilateralFilter(imgGrayScale, 11, 17, 17)
imgEdged = cv2.Canny(bfilter, 30, 200)

# Resize the edged image before displaying
imgEdgedResized = cv2.resize(imgEdged, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
cv2.imshow("Edged Image", imgEdgedResized)

# Find contours
keypoints = cv2.findContours(imgEdged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None

# Identify the location of the number plate
for contour in contours:

    approx = cv2.approxPolyDP(contour, 10, True)

    # Assuming number plate has a rectangle shape
    if len(approx) == 4:
        location = approx
        break

# Create a mask and extract the number plate region
mask = np.zeros(imgGrayScale.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = imgGrayScale[x1:x2 + 1, y1:y2 + 1]

cv2.imshow("Number Plate", cropped_image)

# Perform OCR on the cropped image
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)

# Overlay the recognized text on the original image
text = result[0][-2]
imgFinal = cv2.putText(img, text, (approx[0][0][0], approx[1][0][1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
imgFinal = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)

# Resize the final image before displaying
imgFinalResized = cv2.resize(imgFinal, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
cv2.imshow("Final Image", cv2.cvtColor(imgFinalResized, cv2.COLOR_BGR2RGB))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
