import cv2


def get_contours(image):
    # detect outline/border of a picture
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        cv2.drawContours(imgContour, contour, -1, (255, 0, 0), 3)


img = cv2.imread('images/shape.jpg')
cv2.imshow("Original Picture", img)

imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale", imgGrayScale)

imgBlur = cv2.GaussianBlur(imgGrayScale, (7, 7), 1)
cv2.imshow("Blur Image", imgBlur)

imgCanny = cv2.Canny(imgBlur, 50, 50)
cv2.imshow("Canny Edge Detector", imgCanny)

imgContour = img.copy()
get_contours(imgCanny)
cv2.imshow("Contour Image", imgContour)

cv2.waitKey(0)
