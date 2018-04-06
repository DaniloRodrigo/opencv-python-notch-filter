import sys, cv2
import numpy as numpy

path = sys.argv[1]

image = cv2.imread(path)

roi = cv2.selectROI('Selecte the area ', image, False)
selected_area = image[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

cv2.imshow('Cropped', selected_area)
cv2.waitKey(0)
cv2.destryAllWindows()
