import cv2

cap = cv2.VideoCapture("highway.mp4")

# create background subtractor to differentiate whether objects are moving
# history: to determine number of previous 100 frames to create model background
# varThreshold: if number of px is > 40 then object categorized as foreground instead of background
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:

    ret, frame = cap.read()

    # height and width dimensions for Region of Interest
    roi = frame[340:720, 500:800]

    # store moving objects in video frames into mask variable
    mask = object_detector.apply(roi)

    # create image thresholding to remove shadow (gray) by only keeping white objects
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    # find contours coordinates
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv2.contourArea(contour)

        # draw outline contours if contour area is more than 100
        if area > 100:
            # cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(
                roi,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("ROI", roi)

    key = cv2.waitKey(30)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
