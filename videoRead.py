import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#capture=cv.VideoCapture(0)  # 0 is open your pc camera
capture=cv.VideoCapture('videos/birds.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resize=rescaleFrame(frame, scale=2)
    cv.imshow('Video',frame)
    cv.imshow('Video-Resize',frame_resize)
    if cv.waitKey(20) & 0xFF==ord('d'): # if we push the d on keyboard then it close
        break

capture.release()
cv.destroyAllWindows()