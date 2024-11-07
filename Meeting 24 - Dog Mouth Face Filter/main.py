import cv2
import mediapipe as mp
from math import hypot

cap = cv2.VideoCapture(0)

# set canvas width
cap.set(3, 640)

# set canvas height
cap.set(4, 480)

mouth_img = cv2.imread('mouth.png')

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=4)

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            leftMouthX, leftMouthY = 0, 0
            rightMouthX, rightMouthY = 0, 0
            centerMouthX, centerMouthY = 0, 0

            for lm_id, lm in enumerate(face_landmarks.landmark):

                h, w, c = rgb.shape
                x, y = int(lm.x * w), int(lm.y * h)

                # landmark id for left mouth
                if lm_id == 91:
                    leftMouthX, leftMouthY = x, y

                # landmark id for right mouth
                if lm_id == 128:
                    rightMouthX, rightMouthY = x, y

                # landmark id for center mouth
                if lm_id == 14:
                    centerMouthX, centerMouthY = x, y

            mouth_width = int(hypot(rightMouthX - leftMouthX, rightMouthY - leftMouthY * 1.2))
            mouth_height = int(mouth_width * 0.8)

            if (mouth_width and mouth_height) != 0:
                dog_mouth = cv2.resize(mouth_img, (mouth_width, mouth_height))

            top_left = (int(centerMouthX - mouth_width / 2), int(centerMouthY - mouth_height / 2))
            bottom_right = (int(centerMouthX + mouth_width / 2), int(centerMouthY + mouth_height / 2))
            mouth_area = frame[top_left[1]: top_left[1] + mouth_height, top_left[0]: top_left[0] + mouth_width]

            dog_mouth_gray = cv2.cvtColor(dog_mouth, cv2.COLOR_BGR2GRAY)
            _, dog_mask = cv2.threshold(dog_mouth_gray, 25, 255, cv2.THRESH_BINARY_INV)

            # delete the mouth part
            no_mouth = cv2.bitwise_and(mouth_area, mouth_area, mask=dog_mask)
            final_mouth = cv2.add(no_mouth, dog_mouth)
            frame[top_left[1]: top_left[1] + mouth_height, top_left[0]: top_left[0] + mouth_width] = final_mouth

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
