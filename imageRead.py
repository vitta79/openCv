import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img=cv.imread('images/bird-large.jpg')
img_resize=rescaleFrame(img)
cv.imshow('Bird',img)
cv.imshow('Bird-Resize',img_resize)
cv.waitKey(0)

