#import numpy as np
#import cv2 as cv
#
##Load a color image in grayscale
#img = cv.imread('messi5.jpg', 0)
#
#
##cv.imshow('image', img)
##cv.waitKey(0)
##cv.destroyAllWindow()
#
#
#cv.namedWindow('image', cv.WINDOW_NORMAL)
#cv.imshow('image',img)
#cv.waitKey(0)
#cv.destroyAllWindows()


import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()