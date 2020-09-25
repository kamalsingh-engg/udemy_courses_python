import cv2
im_g = cv2.imread("smallgray.png",0) # 0 is here for gray image and 1 is here for the rgb image
print(im_g)

cv2.imwrite("biggray.jpg",im_g)