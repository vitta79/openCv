import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('images/bird.jpg')
#cv.imshow('bird',img)
#cv.waitKey()
plt.imshow(img)  # plt shows us BGR not RGB because we read the image with opencv and we try show it using matplotlib
plt.show()       # on plt color order is RGB(RED, GREEN, BLUE), on openCv color order BGR

# during this we change the color order
img_plt=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_plt)
plt.show()

# make gray
img_gray=cv.imread('images/bird.jpg',cv.IMREAD_GRAYSCALE)
plt.imshow(img_gray,cmap='gray')
plt.show()

# resize the image
#img_resize=cv.resize(img,(500,300))
width=0.8
height=0.2
img_resize=cv.resize(img,(0,0),img,width,height)
plt.imshow(img_resize)
plt.show()

# ters cevirme
img_ters=cv.flip(img,0) # 0- can be 1 or -1
plt.imshow(img_ters)
plt.show()
print(cv.imwrite('images/bird_ters.jpg',img_ters))