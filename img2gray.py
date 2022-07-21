import cv2 as cv
# path of image. You change to your image path
img_path='images/bird.jpg'

# taking gray image from org image
img=cv.imread(img_path,cv.IMREAD_GRAYSCALE)

# if success then write true or false
print(cv.imwrite('images/img_gray.jpg',img))

