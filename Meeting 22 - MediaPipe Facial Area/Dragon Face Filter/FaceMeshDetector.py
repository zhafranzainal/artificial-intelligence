import mediapipe as mp
import numpy as np


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
