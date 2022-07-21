import cv2 as cv
import numpy as np

## Function ##
def drawCircle(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(blank, center=(x,y), radius=50, color=(255,0,0), thickness=-1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(blank, pt1=(x,y),pt2=(x+100,y+100), color=(2,0,0), thickness=5)

cv.namedWindow(winname='blank_Page')
cv.setMouseCallback('blank_Page',drawCircle)

blank=np.zeros((512,512),dtype=np.int8)

while True:
    cv.imshow('blank_Page',blank)
    if cv.waitKey(20) & 0xFF==27:
        break
cv.destroyAllWindows()
