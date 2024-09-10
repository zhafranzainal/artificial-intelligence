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

            # draw rectangle indicating selection mode
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

        if fingers[1] and fingers[2] is False:

            print("Drawing Mode")

            # draw circle indicating drawing mode
            cv2.circle(frame, (x1, y1), 15, drawColor, cv2.FILLED)

            # if brush coordinate still at initial coordinate, overwrite with tip index finger nodes landmark location
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            # if choose eraser mode
            if drawColor == (0, 0, 0):
                cv2.line(frame, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            # else choose brush colour
            else:
                cv2.line(frame, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    frame[0: 125, 0:1280] = header

    cv2.imshow("Frame", frame)
    cv2.imshow("Canvas", imgCanvas)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
