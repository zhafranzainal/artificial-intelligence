import cv2
import mediapipe as mp
from math import hypot

cap = cv2.VideoCapture(0)

# set canvas width
cap.set(3, 640)

# set canvas height
cap.set(4, 480)

nose_img = cv2.imread('pig_nose.png')

mpDraw = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=4)

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # mpDraw.draw_landmarks(image=frame, landmark_list=face_landmarks,
            #                       connections=mpFaceMesh.FACEMESH_TESSELATION, landmark_drawing_spec=None,
            #                       connection_drawing_spec=mpDrawingStyles.get_default_face_mesh_tesselation_style()
            #                       )
            # mpDraw.draw_landmarks(image=frame, landmark_list=face_landmarks,
            #                       connections=mpFaceMesh.FACEMESH_CONTOURS, landmark_drawing_spec=None,
            #                       connection_drawing_spec=mpDrawingStyles.get_default_face_mesh_contours_style()
            #                       )

            leftNoseX = 0
            leftNoseY = 0
            rightNoseX = 0
            rightNoseY = 0
            centerNoseX = 0
            centerNoseY = 0

            for lm_id, lm in enumerate(face_landmarks.landmark):

                h, w, c = rgb.shape
                x, y = int(lm.x * w), int(lm.y * h)

                # landmark id for left nose
                if lm_id == 49:
                    leftNoseX, leftNoseY = x, y

                # landmark id for right nose
                if lm_id == 279:
                    rightNoseX, rightNoseY = x, y

                # landmark id for center nose
                if lm_id == 5:
                    centerNoseX, centerNoseY = x, y

            nose_width = int(hypot(rightNoseX - leftNoseX, rightNoseY - leftNoseY * 1.2))
            nose_height = int(nose_width * 0.8)

            if (nose_width and nose_height) != 0:
                pig_nose = cv2.resize(nose_img, (nose_width, nose_height))

            top_left = (int(centerNoseX - nose_width / 2), int(centerNoseY - nose_height / 2))
            bottom_right = (int(centerNoseX + nose_width / 2), int(centerNoseY + nose_height / 2))
            nose_area = frame[top_left[1]: top_left[1] + nose_height, top_left[0]: top_left[0] + nose_width]

            pig_nose_gray = cv2.cvtColor(pig_nose, cv2.COLOR_BGR2GRAY)
            _, nose_mask = cv2.threshold(pig_nose_gray, 25, 255, cv2.THRESH_BINARY_INV)

            # delete the nose part
            no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
            final_nose = cv2.add(no_nose, pig_nose)
            frame[top_left[1]: top_left[1] + nose_height, top_left[0]: top_left[0] + nose_width] = final_nose

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
