import cv2 as cv
import numpy as np

blank=np.zeros((500, 700, 3), dtype='uint8')
cv.imshow('Blank', blank)

cv.rectangle(blank, (10,50), (250,250),(250,0,0),thickness=2)
cv.imshow('Rectangle',blank)
cv.waitKey(0)