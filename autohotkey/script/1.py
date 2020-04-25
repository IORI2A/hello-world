

import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
#cv.imshow('image', img)
#cv.waitKey(0)

px = img[100, 100]
#px = img[100,100]
print(px)

blue = img[100, 100, 0]
print(blue)

rgb = img[100, 100, 0]
print('0: {0}'.format(rgb))
rgb = img[100, 100, 1]
print('1: {0}'.format(rgb))
rgb = img[100, 100, 2]
print('2: {0}'.format(rgb))


img[100, 100] = [255, 255, 255]
print(img[100, 100])

#cv.imshow('image', img)
cv.imshow('image img[100, 100] = [255, 255, 255]', img)
cv.waitKey(0)

img[100, 100] = [85, 97, 103]
print(img[100, 100])

#cv.imshow('image ', img)
cv.imshow('image img[100, 100] = [85, 97, 103]', img)
cv.waitKey(0)

#Better pixel accessing and editing method :
# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

red = img.item(10,10,2)
print(red)
redset = img.itemset((10,10,2),200)
print(redset)
red = img.item(10,10,2)
print(red)


print( img.shape )
print( img.size )
print( img.dtype )


#ball = img[280:340, 330:390]
#img[273:333, 100:160] = ball
#
#cv.imshow('image', img)
#cv.waitKey(0)

#ball = img[286:246, 338:289]
#img[56:246, 108:289] = ball
#
#cv.imshow('image', img)
#cv.waitKey(0)

#ball = img[0:0, 100:100]
#cv.imshow('ball', ball)
#cv.waitKey(0)

#ball = img[286:338, 246:289]
#cv.imshow('ball', ball)
#cv.waitKey(0)
#
#
#img[56:108, 246:289] = ball
#cv.imshow('image ball', img)
#cv.waitKey(0)


#ball = img[200:260, 230:290]
#cv.imshow('ball', ball)
#cv.waitKey(0)
#
#
#img[193:253, 00:60] = ball
#cv.imshow('image ball', img)
#cv.waitKey(0)

ball = img[246:289, 286:338]
cv.imshow('ball', ball)
cv.waitKey(0)


img[246:289, 56:108] = ball
cv.imshow('image ball', img)
cv.waitKey(0)


