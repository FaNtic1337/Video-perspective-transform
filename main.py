import cv2
import numpy as np

cap = cv2.VideoCapture('Video.mp4')

while True:

    _, frame = cap.read()

    cv2.circle(frame, (640, 410), 5, (0, 0, 255), -1)
    cv2.circle(frame, (1210, 390), 5, (0, 0, 255), -1)
    cv2.circle(frame, (210, 880), 5, (0, 0, 255), -1)
    cv2.circle(frame, (1650, 840), 5, (0, 0, 255), -1)

    pts1 = np.float32([[640, 410], [1210, 390], [210, 880], [1650, 840]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))

    cv2.imshow('Frame', result)

    key = cv2.waitKey(1)




cap.release()
cv2.destroyAllWindows()