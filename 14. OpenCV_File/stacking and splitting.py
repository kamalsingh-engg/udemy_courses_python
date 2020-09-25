""""
stacking means to continous add  the data into symtery  ,stack only required one argumnent so here i am trying to
send it in tupple
hstack means horizontal stacking
vstack means vertical stacking
"""
import cv2
import numpy as np
im_g = cv2.imread("smallgray.png",0)
#st_output = np.hstack((im_g,im_g))
#print(st_output)
st = np.hstack((im_g,im_g,im_g))
#print(st)

st1 = np.vstack((im_g,im_g,im_g))
#print(st1)


"""
we understand the concept of stacking and now we will discuss on the concept of the splitting 

splitting means to divide the system into the equal so we have to take care of its equality 

similarly as it works in case of stacking the same concept is in the spliting

vsplit - vertical splitting 
hsplit - horizontal splitting 
"""

st2 = np.hsplit(st1,5)
#print(st2)

st3 = np.vsplit(st1,3)
print(st3)