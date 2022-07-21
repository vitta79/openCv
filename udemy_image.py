import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from PIL import Image
img=Image.open('images/bird.jpg')
print(type(img))
img_arr=np.asarray(img)
print(type(img_arr))
print(img_arr.shape)
plt.imshow(img_arr[:,:,2],cmap='gray') # 0 is Red, 1 is Green, 2 is Blue
plt.show()

copy=img_arr.copy()
#copy[:,:,0]=0 # no red color
#copy[:,:,1]=0 # no green color
copy[:,:,2]=0 # no blue color
plt.imshow(copy)
plt.show()

