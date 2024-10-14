import cv2
import mediapipe as mp


def plot_landmark(image_frame, facial_landmarks, facial_area_obj):
    for source_idx, target_idx in facial_area_obj:
        source = facial_landmarks.landmark[source_idx]
        target = facial_landmarks.landmark[target_idx]
        relative_source = (int(image_frame.shape[1] * source.x), int(image_frame.shape[0] * source.y))
        relative_target = (int(image_frame.shape[1] * target.x), int(image_frame.shape[0] * target.y))
        cv2.line(image_frame, relative_source, relative_target, (255, 255, 255), thickness=2)


cap = cv2.VideoCapture(0)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

while True:

    ret, frame = cap.read()

    results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        plot_landmark(frame, landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
