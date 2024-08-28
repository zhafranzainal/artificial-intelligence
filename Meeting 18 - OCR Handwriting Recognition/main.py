from tensorflow.keras.models import load_model
from imutils.contours import sort_contours

import cv2
import imutils
import numpy as np

print("Load the model ....")
model = load_model("handwriting.h5")

img = cv2.imread("images/1.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgEdged = cv2.Canny(imgBlur, 30, 150)

contours = cv2.findContours(imgEdged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sort_contours(contours, method="left-to-right")[0]
print(contours)

characters = []

for contour in contours:

    (x, y, width, height) = cv2.boundingRect(contour)

    # make sure bounding box size is neither too big nor too small based on width and height dimension
    if (5 <= width <= 150) and (15 <= height <= 120):

        # region of interest
        imgRoi = imgGray[y:y + height, x:x + width]

        # change image into black (low light intensity) and white (high light intensity)
        thresh = cv2.threshold(imgRoi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        (threshHeight, threshWidth) = thresh.shape

        # change ROI area size into 32px
        if threshWidth > threshHeight:
            thresh = imutils.resize(thresh, width=32)
        else:
            thresh = imutils.resize(thresh, height=32)

        (threshHeight, threshWidth) = thresh.shape
        dX = int(max(0, 32 - threshWidth) / 2.0)
        dY = int(max(0, 32 - threshHeight) / 2.0)

        # add border
        padded = cv2.copyMakeBorder(thresh, top=dY, bottom=dY, left=dX, right=dX,
                                    borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0)
                                    )

        # add padding
        padded = cv2.resize(padded, (32, 32))

        # change scale pixel intensities that have a range of 0 - 255 become 0 - 1 with float data type
        padded = padded.astype("float32") / 255.0

        # add dimension from Numpy Array padded picture that has 1 dimension in the beginning into 2 dimensions
        padded = np.expand_dims(padded, axis=-1)

        # add into list in the form of a tuple
        characters.append(
            (padded, (x, y, width, height))
        )

# boundingBox coordinate from each character
boxes = [b[1] for b in characters]

# image of each character that has been padded before
characters = np.array([character[0] for character in characters], dtype="float32")

# identify character based on model that has been loaded before
predictions = model.predict(characters)
labelNames = "0123456789"
labelNames += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
labelNames = [labelName for labelName in labelNames]

for (prediction, (x, y, w, h)) in zip(predictions, boxes):
    # find index with the highest probability value
    i = np.argmax(prediction)

    # match character found with labelName index list that has been made
    probability = prediction[i]
    label = labelNames[i]

    print("[INFO] {} - {:.2f}%".format(label, probability * 100))

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
