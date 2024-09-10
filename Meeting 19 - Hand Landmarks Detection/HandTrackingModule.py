import mediapipe as mp
import cv2


class HandDetector:

    def __init__(self, mode=False, max_hands=2, model_complexity=1, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.maxHands = max_hands
        self.modelComplexity = model_complexity
        self.detectionConfidence = detection_confidence
        self.trackConfidence = track_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.modelComplexity, self.detectionConfidence, self.trackConfidence
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None
        self.landmarkList = None

    def find_hands(self, frame, draw=True):

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(frame_rgb)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame

    def find_position(self, frame, hand_no=0, draw=True):

        self.landmarkList = []

        if self.results.multi_hand_landmarks:

            my_hand = self.results.multi_hand_landmarks[hand_no]

            for index, landmark in enumerate(my_hand.landmark):

                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                self.landmarkList.append([index, cx, cy])

                if draw:
                    cv2.circle(frame, (cx, cy), 7, (255, 0, 0), cv2.FILLED)

        return self.landmarkList
