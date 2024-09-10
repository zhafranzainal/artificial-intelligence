import cv2
import os
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

while True:

    res, frame = cap.read()

    # flip frames horizontally
    frame = cv2.flip(frame, 1)
    frame = detector.find_hands(frame)
    landmarkList = detector.find_position(frame, draw=True)
    print(landmarkList)

    frame[0: 125, 0:1280] = header

    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
