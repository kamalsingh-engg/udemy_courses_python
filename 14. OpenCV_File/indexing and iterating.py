import cv2
im_g = cv2.imread("smallgray.png",0)
#print(im_g)
img1 = im_g[1:3]   # that we don't need to define the columns as it is by-default accessed
#print(img1)
img2 = im_g[1:3,2:4]
#print(img2)
"""
the above code is as for the indexing as similar as the list now we will check the iterating 
"""

#for i in im_g:
#    print(i)   # this is iterate as usual

#for i in im_g.T:
#    print(i)    # this is iterate of the data which is transpose

for i in im_g.flat:
    print(i)



