import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blank=np.zeros(shape=(512,512),dtype=np.int16)

# shapes on img
cv.rectangle(blank, pt1=(10,10), pt2=(300,200), color=(255,0,0), thickness=5)
cv.rectangle(blank, pt1=(300,300), pt2=(500,500), color=(152,0,0), thickness=10)

cv.circle(blank, center=(100,400), radius=75, color=(255,0,0), thickness=7)
cv.circle(blank, center=(400,100), radius=75, color=(200,0,0), thickness=-1) # -1 fulls the circle

cv.line(blank, pt1=(0,220), pt2=(250,300),color=(130,0,0), thickness=4)

# star shape
vertices=np.array([[55,190],[105,120],[45,75],[120,75],[160,15],[200,75],[275,75],[215,120],[265,190],[160,150]], dtype=np.int32)
pts=vertices.reshape((-1,1,2))
cv.polylines(blank,[pts],isClosed=True, color=(255,0,0),thickness=3)
print(vertices.shape)

# Text on img
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(blank, text='Vitta',org=(340, 250), fontFace=font, color=(255,0,0), thickness=4, fontScale=2, lineType=cv.LINE_AA)
cv.putText(blank, text='violetta',org=(350, 400), fontFace=font, color=(255,0,0), thickness=2, fontScale=1, lineType=cv.LINE_AA)
# writes on star shape
cv.putText(blank, text='star',org=(13   0, 120), fontFace=font, color=(255,0,0), thickness=4, fontScale=1, lineType=cv.LINE_AA)
plt.imshow(blank)
plt.show()
