import cv2
import numpy as np

# Minimum confidence model value when detecting objects
min_confidence = 0.6

# List of labels for the Common Objects in Context (COCO) dataset
classes = [
    'background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
    'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
]

colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Parameter 1: Prototxt file which is the structure of the neural network graph model that will be used later
# Parameter 2: .caffemodel file which is a pre-trained Caffe model file for object detection
net = cv2.dnn.readNetFromCaffe(
    "models/MobileNetSSD_deploy.prototxt.txt",
    "models/MobileNetSSD_deploy.caffemodel"
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
    detected_objects = net.forward()

    for i in range(0, detected_objects.shape[2]):

        # Index 2 stores information on the confidence value of the object detection results
        confidence = detected_objects[0, 0, i, 2]

        # Only take object detection results with a minimum confidence value of 60%
        if confidence > min_confidence:
            # Access and calculate the location of the coordinates around the object detection result area
            # Index 1 stores classes object of detected object
            # Index 3-6 store coordinate information of detected object
            # 3: StartX, 4: StartY, 5: endX, 6: endY
            class_id = int(detected_objects[0, 0, i, 1])
            print(classes[class_id])

            prediction_text = f"{classes[class_id]}: {confidence:.2f}"
            box = detected_objects[0, 0, i, 3:7] * np.array([width, height, width, height])

            (startX, startY, endX, endY) = box.astype('int')

            # Change the position of the text confidence value by 15px down if the text passes through the image area
            y = startY - 15 if startY > 30 else startY + 15

            cv2.rectangle(
                frame,
                (startX, startY),
                (endX, endY),
                colors[class_id],
                2
            )

            # Display the confidence/probability value text at the top of the red box on the object
            cv2.putText(
                frame,
                prediction_text,
                (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                colors[class_id],
                2
            )

    cv2.imshow("Frame", frame)

    # Stop looping to display video frames when 'q' button is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
