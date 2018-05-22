import numpy as np;
from matplotlib import pyplot as plt
import cv2

myimage = cv2.imread("Efes.JPG",-1);
myimage_grayscale = cv2.cvtColor(myimage,cv2.COLOR_BGR2GRAY)
#get dimension
print(myimage.shape)

#get pixel 
px = myimage[100,100]
print("Pixel Blue {} , Green {} , Red {}".format(px[0],px[1],px[2]));

#set pixel 
myimage[100,100] = [255,255,255]
px = myimage[100,100]
print("Pixel Blue {} , Green {} , Red {}".format(px[0],px[1],px[2]));

#region setting
region = myimage[280:940, 330:1090]
myimage[273:933, 100:860] = region

RGB_image =  cv2.cvtColor(myimage, cv2.COLOR_BGR2RGB) 
plt.imshow(RGB_image)
plt.show();

#histograms
 #grey Image 
plt.hist(myimage_grayscale.ravel(),256,[0,256])
plt.title("Gray image histogram")
plt.show()

hist = cv2.calcHist([myimage],[0],None,[256],[0,256])
plt.hist(hist);
plt.title("blue channel histogram")
plt.show();


hist = cv2.calcHist([myimage],[1],None,[256],[0,256])
plt.hist(hist);
plt.title("green channel histogram")
plt.show();

hist = cv2.calcHist([myimage],[2],None,[256],[0,256])
plt.hist(hist);
plt.title("red channel histogram")
plt.show();


#cv2.imshow('image',myimage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
