import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 960)

left_eye = cv2.imread('assets/eye1.png')
right_eye = cv2.imread('assets/eye2.png')

smoke_animation = cv2.VideoCapture('assets/smoke_animation.mp4')
smoke_frame_counter = 0

while True:

    ret, frame = cap.read()
    ret, smoke_frame = smoke_animation.read()

    smoke_frame_counter += 1

    # Reset frames to 0 once finished to keep looping animation
    if smoke_frame_counter == smoke_animation.get(cv2.CAP_PROP_FRAME_COUNT):
        smoke_animation.set(cv2.CAP_PROP_POS_FRAMES, 0)
        smoke_frame_counter = 0

    frame = cv2.flip(frame, 1)

    cv2.imshow('Frame', smoke_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
