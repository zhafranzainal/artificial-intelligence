import cv2

cap = cv2.VideoCapture(0)

# set canvas width
cap.set(3, 640)

# set canvas height
cap.set(4, 480)

while True:

    ret, frame = cap.read()
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
