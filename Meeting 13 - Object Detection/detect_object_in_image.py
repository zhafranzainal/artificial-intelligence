import cv2
import numpy as np

# Minimum confidence model value when detecting objects
min_confidence = 0.6

# List of labels for the Common Objects in Context (COCO) dataset
classes = [
    'background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
    'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
]

# Parameter 1: Prototxt file which is the structure of the neural network graph model that will be used later
# Parameter 2: .caffemodel file which is a pre-trained Caffe model file for object detection
net = cv2.dnn.readNetFromCaffe(
    "models/MobileNetSSD_deploy.prototxt.txt",
    "models/MobileNetSSD_deploy.caffemodel"
)

image = cv2.imread('images/1.jpg')
image = cv2.resize(image, (800, 600))

# Retrieve image height and width dimension data
height, width = image.shape[0], image.shape[1]

blob = cv2.dnn.blobFromImage(
    cv2.resize(image, (300, 300)),
    0.007843,  # image size setting with a calculation of 1/n, where n is the scale factor that we determine
    (300, 300),  # another dimension that is often used is 229x229 or 224x224
    127.5  # BGR pixel values as Mean Subtraction caffe model used is GoogLeNet
)

net.setInput(blob)
detected_objects = net.forward()

# Looping for each object detected in the image
for i in range(detected_objects.shape[2]):

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

        # Change the position of the text confidence value by 10px down if the text passes through the image area
        y = startY - 15 if startY > 30 else startY + 15

        cv2.rectangle(
            image,
            (startX, startY),
            (endX, endY),
            (0, 0, 255),
            2
        )

        # Display the confidence/probability value text at the top of the red box on the object
        cv2.putText(
            image,
            prediction_text,
            (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2
        )

cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
