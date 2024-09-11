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

    def fingers_up(self):

        fingers = []

        # list for the ID nodes of fingertip landmarks
        tip_ids = [4, 8, 12, 16, 20]

        # condition to check if thumb is up
        if self.landmarkList[tip_ids[0]][1] < self.landmarkList[tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # index for the fingers from index finger to pinky finger
        for finger_id in range(1, 5):
            if self.landmarkList[tip_ids[finger_id]][2] < self.landmarkList[tip_ids[finger_id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
