import mediapipe as mp
import numpy as np
import itertools
import cv2


class FaceMesh:

    def __init__(self):

        self.mpFaceDetection = mp.solutions.face_detection

        self.face_detection = self.mpFaceDetection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh

        self.faceMeshImages = self.mpFaceMesh.FaceMesh(
            static_image_mode=True, max_num_faces=2, min_detection_confidence=0.5
        )

        self.faceMeshVideos = self.mpFaceMesh.FaceMesh(
            static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.3
        )

        self.mpDrawStyles = mp.solutions.drawing_styles

    def detect_facial_landmarks(self, image, face_mesh):

        results = face_mesh.process(image[:, :, ::-1])

        # copy image from provided parameter
        output_image = image[:, :, ::-1].copy()

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mpDrawStyles.get_default_face_mesh_tesselation_style()
                )
                self.mpDraw.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mpDrawStyles.get_default_face_mesh_contours_style()
                )

        return np.ascontiguousarray(output_image[:, :, ::-1], dtype=np.uint8), results

    def get_size(self, image, face_landmarks, index):

        image_height, image_width, _ = image.shape

        # convert indexes value in the form of Dictionary of Tuples into a regular list
        index_list = list(itertools.chain(*index))

        landmarks = []

        # find coordinates of each landmark in a certain face area
        for index in index_list:
            landmarks.append([
                int(face_landmarks.landmark[index].x * image_width),
                int(face_landmarks.landmark[index].y * image_height)
            ])

        _, _, width, height = cv2.boundingRect(np.array(landmarks))
        landmarks = np.array(landmarks)

        return width, height, landmarks

    def is_open(self, image, face_mesh_results, face_part, threshold=5):

        image_height, image_width, _ = image.shape
        output_image = image.copy()
        face_status = {}

        if face_part == 'MOUTH':
            indexes = self.mpFaceMesh.FACEMESH_LIPS
        elif face_part == 'LEFT EYE':
            indexes = self.mpFaceMesh.FACEMESH_LEFT_EYE
        elif face_part == 'RIGHT EYE':
            indexes = self.mpFaceMesh.FACEMESH_RIGHT_EYE
        else:
            return

        for face_no, face_landmarks in enumerate(face_mesh_results.multi_face_landmarks):

            _, height, _ = self.get_size(image, face_landmarks, indexes)
            _, face_height, _ = self.get_size(image, face_landmarks, self.mpFaceMesh.FACEMESH_FACE_OVAL)

            if (height / face_height) * 100 > threshold:
                face_status[face_no] = 'OPEN'
                color = (0, 255, 0)
            else:
                face_status[face_no] = 'CLOSE'
                color = (0, 0, 255)

            cv2.putText(
                output_image,
                f'FACE {face_no + 1} {face_part} {face_status[face_no]}.',
                (10, image_height - 40),
                cv2.FONT_HERSHEY_PLAIN,
                1.4, color, 2
            )

            return output_image, face_status

    def masking(self, image, filter_img, face_landmarks, face_part, indexes):

        annotated_image = image.copy()

        try:
            filter_img_height, filter_img_width, _ = filter_img.shape
            _, face_part_height, landmarks = self.get_size(image, face_landmarks, indexes)
            required_height = int(face_part_height * 2.5)

            resized_filter_img = cv2.resize(
                filter_img,
                (int(filter_img_width * (required_height / filter_img_height)), required_height)
            )

            filter_img_height, filter_img_width, _ = resized_filter_img.shape

            _, filter_img_mask = cv2.threshold(
                cv2.cvtColor(resized_filter_img, cv2.COLOR_BGR2GRAY),
                25, 255,
                cv2.THRESH_BINARY_INV
            )

            center = landmarks.mean(axis=0).astype("int")

            if face_part == 'MOUTH':
                location = (int(center[0] - filter_img_width / 3), int(center[1]))
            else:
                location = (int(center[0] - filter_img_width / 2), int(center[1] - filter_img_height / 2))

            ROI = image[location[1]: location[1] + filter_img_height, location[0]: location[0] + filter_img_width]
            resultant_image = cv2.bitwise_and(ROI, ROI, mask=filter_img_mask)
            resultant_image = cv2.add(resultant_image, resized_filter_img)

            annotated_image[
            location[1]: location[1] + filter_img_height,
            location[0]: location[0] + filter_img_width
            ] = resultant_image

        except Exception as e:
            pass

        return annotated_image
