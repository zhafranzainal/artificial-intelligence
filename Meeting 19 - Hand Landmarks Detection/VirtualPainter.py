import cv2
import os
import numpy as np
import HandTrackingModule as Htm

detector = Htm.HandDetector(detection_confidence=0.85)

cap = cv2.VideoCapture(0)

# set canvas width
cap.set(3, 1280)

# set canvas height
cap.set(4, 720)

myListDirectory = os.listdir("header")
print(myListDirectory)
overlayList = []

for imPath in myListDirectory:
    image = cv2.imread(f'header/{imPath}')
    overlayList.append(image)

header = overlayList[0]

# default brush color is red
drawColor = (0, 0, 255)
brushThickness = 7
eraserThickness = 40

# brush start coordinates
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:

    res, frame = cap.read()

    # flip frames horizontally
    frame = cv2.flip(frame, 1)
    frame = detector.find_hands(frame)
    landmarkList = detector.find_position(frame, draw=True)
    print(landmarkList)

    if len(landmarkList) != 0:
        x1, y1 = landmarkList[8][1:]
        x2, y2 = landmarkList[12][1:]
        print(x1, y1, x2, y2)

        fingers = detector.fingers_up()
        print(fingers)

        # if index and middle finger are lifted
        if fingers[1] and fingers[2]:

            xp, yp = 0, 0
            print("Selection mode")

            # draw rectangle
            cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

            if y1 < 125:
                if 320 < x1 < 480:
                    header = overlayList[0]
                    drawColor = (0, 0, 255)
                elif 480 < x1 < 630:
                    header = overlayList[1]
                    drawColor = (0, 255, 0)
                elif 630 < x1 < 840:
                    header = overlayList[2]
                    drawColor = (255, 0, 0)
                elif x1 > 1000:
                    header = overlayList[3]
                    # black color as the eraser mode
                    drawColor = (0, 0, 0)

    frame[0: 125, 0:1280] = header

    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
