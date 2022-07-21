import numpy as np
import cv2 as cv


drawing= False
x1, y1=-1, -1
def draw_rectangle(event, x,y ,flags, params):
    global  x1, y1, drawing
    if event== cv.EVENT_LBUTTONDOWN:
        drawing= True
        x1, y1= x,y
    elif event==cv.EVENT_MOUSEMOVE:
        if drawing==True:
            cv.rectangle(img, (x1,y1),(x,y),(255,0,0),-1)
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False
        cv.rectangle(img, (x1, y1), (x, y), (255, 0, 0), -1)

cv.namedWindow(winname='drawing')
cv.setMouseCallback('drawing',draw_rectangle)

img=np.zeros((512,512))
while True:
    cv.imshow('drawing', img)
    if cv.waitKey(20) & 0xFF==27:
        break
cv.destroyAllWindows()