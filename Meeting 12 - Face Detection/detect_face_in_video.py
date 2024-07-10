import cv2
import numpy as np

# Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
min_confidence = 0.5

# Parameter 1: Prototxt file which is the structure of the neural network graph model that will be used later
# Parameter 2: .caffemodel file which is a pre-trained Caffe model file for face detection
net = cv2.dnn.readNetFromCaffe(
    "models/deploy.prototxt.txt",
    "models/res10_300x300_ssd_iter_140000.caffemodel"
)

# Webcam index
cap = cv2.VideoCapture(0)

while True:

    # return True/False as an indicator of whether the video frames were successfully read
    # return a Numpy Array representing the image frames that have been read
    ret, frame = cap.read()

    # Access the image size, namely height, width and stored in variables height, width
    height, width = frame.shape[0], frame.shape[1]

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        1.0,  # image size setting with a calculation of 1/n, where n is the scale factor that we determine
        (300, 300),  # another dimension that is often used is 229x229 or 224x224
        (104.0, 117.0, 123.0)  # BGR pixel values as Mean Subtraction caffe model used is GoogLeNet
    )

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):

        # Index 2 stores information on the confidence value of the face detection results
        confidence = detections[0, 0, i, 2]

        # If the confidence value is greater, then the probability/confidence value
        # will be displayed around the face detection result area
        if confidence > min_confidence:
            # Access and calculate the location of the coordinates around the face detection result area
            # Index 3-6 store coordinate information of faces that have been detected
            # 3: StartX, 4: StartY, 5: endX, 6: endY
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype('int')
            text = "{:.2f}%".format(confidence * 100)

            # Change the position of the text confidence value by 10px down if the text passes through the image area
            y = startY - 10 if startY - 10 > 10 else startY + 10

            cv2.rectangle(
                frame,
                (startX, startY),
                (endX, endY),
                (0, 0, 255),
                2
            )

            # Display the confidence/probability value text at the top of the red box on the face
            cv2.putText(
                frame,
                text,
                (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 0, 255),
                2
            )

    cv2.imshow("Frame", frame)

    # Stop looping to display video frames when 'q' button is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
