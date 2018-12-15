import cv2
import numpy as np


def janelamento(img, windowsize_c, windowsize_r):
    height, width = img.shape

    x=int(height/windowsize_r)
    y=int(width/windowsize_c)

    xi=height%windowsize_r
    yi=width%windowsize_c

    ci=(x*windowsize_r)+windowsize_r
    ri=(y*windowsize_c)+windowsize_c
    img_w={}
    i=0
    if(xi!=0) and(yi!=0):
        img_n= np.zeros((ci, ri))
      
    elif (xi!=0) and(yi==0):
        img_n= np.zeros((height, ri))
      
    elif (xi!=0) and(yi==0):
        img_n= np.zeros((ci, ri))
       

    elif(xi==0) and(yi==0):
        img_n= np.zeros((height, width))
       

 
    height2, width2 = img_n.shape
    
    for r in range(0,height2, 1):
        for c in range(0,width2, 1):
            if r<height and c<width:
                img_n[r,c]=img[r,c]
            else:
                img_n[r,c]=0



   
    for r in range(0,height2, windowsize_r):
        for c in range(0,width2, windowsize_c):
            
            img_w[i]=img_n[r:r+windowsize_r , c:c+windowsize_c]
            i += 1
    return img_w




def montar(img_m,height,width):
    m=0

    windowsize_r, windowsize_c =img_m[0].shape
    

    x=int(height/windowsize_r)
    y=int(width/windowsize_c)

    xi=height%windowsize_r
    yi=width%windowsize_c


    ci=(x*windowsize_r)+windowsize_r
    ri=(y*windowsize_c)+windowsize_c

    i=0
    if(xi!=0) and (yi!=0):
        hsv2= np.zeros((ci, ri))
    elif (yi!=0):
       
        hsv2= np.zeros((ci, width))
    elif (xi!=0):
        
        hsv2= np.zeros((height, ri))
    elif (xi==0) and (yi==0) :
        hsv2 = np.zeros((height, width))
     

    for r in range(0,height,  windowsize_r):
        for c in range(0,width,  windowsize_c):
                hsv2[r:r+ windowsize_r , c:c+ windowsize_c]= img_m[m]
                m=m+1
        
        
    return hsv2