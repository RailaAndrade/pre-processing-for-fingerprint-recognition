import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
from PIL import Image, ImageDraw, ImageFont
import math
import argparse
import aux
import orientacao
import janelamento


 # ----------------------------------------auxiliares------------------------------------


def soma_nc(img,height,width):
    
    soma=0
    for r in range(0,height, 1):
        for c in range(0,width, 1):
            soma=soma+img[r,c]
        
    return soma



def soma_var(img,height,width,u):
    soma=0  
    for r in range(0,height, 1):
        for c in range(0,width, 1):
            soma=soma+(aux.pow2(img[r,c]-u))
    return soma

def norm(img):
    height, width = img.shape
    
    for r in range(0,height, 1):
        for c in range(0,width, 1):
          img[r,c]= img[r,c] *(1.0/255)
    return img


def calcvar(img):
    height, width = img.shape
    u=soma_nc(img,height,width)/(height*width)
    v=soma_var(img,height,width,u)/((height*width)-1)
    return v


def normalizacao(img,u0,v0):
    height, width = img.shape

    #img=img.astype(np.uint8)
    #u valor médio da imagem
    
    u=soma_nc(img,height,width)/(height*width)

    #u0 valor médio esperado
    v=soma_var(img,height,width,u)/((height*width)-1)
    
 
    if v < 0.02:
     
        #img=cv2.equalizeHist(img)
        #img = cv2.medianBlur(img,3)
        #img = cv2.bilateralFilter(img,9,75,75)
        
        kernel = np.array(( [[-1, -1, -1 ,-1 ,-1],[-1, 2, 2 ,2 ,-1],[-1, 2, 3, 2, -1],[-1, 2, 2 ,2 ,-1],[-1, -1, -1 ,-1 ,-1] ]),dtype="int")*1/3
        img= cv2.filter2D(img,-1,kernel)
       
      
        
    
        #u=soma_nc(img,height,width)/(height*width)
        #v=soma_var(img,height,width,u)/((height*width)-1)



    img_norm= np.zeros((height, width))
   
   

    for r in range(0,height, 1):
        for c in range(0,width, 1):

            if(img[r,c]>u):
                img_norm[r,c]=u0+aux.sqrt((aux.pow2(img[r,c]-u))*(v0/v))
                if v==0:
                    img_norm[r,c]=u0+aux.sqrt((aux.pow2(img[r,c]-u))*(v0))
            else:
                img_norm[r,c]=u0-aux.sqrt((aux.pow2(img[r,c]-u))*(v0/v))
                if v==0:
                    img_norm[r,c]=u0-aux.sqrt((aux.pow2(img[r,c]-u))*(v0))
    return img_norm
 
def montar_normalizacao(img_m,height,width,u0,v0):
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
    elif (yi!=0) and(xi==0):
       hsv2= np.zeros((height, ri))
      
    elif (yi==0) and(xi!=0):
        hsv2= np.zeros((ci, width))

        hsv2= np.zeros((height, ri))
    elif (xi==0) and (yi==0) :
        hsv2 = np.zeros((height, width))
     
    
    for r in range(0,height,  windowsize_r):
        for c in range(0,width,  windowsize_c):
                img=normalizacao(img_m[m].astype(np.float),u0,v0)
                hsv2[r:r+ windowsize_r , c:c+ windowsize_c]= img
                m=m+1
        
        
    return hsv2





'''def segmentacao(img):
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
    elif (yi!=0) and(xi==0):
       hsv2= np.zeros((height, ri))
      
    elif (yi==0) and(xi!=0):
        hsv2= np.zeros((ci, width))

        hsv2= np.zeros((height, ri))
    elif (xi==0) and (yi==0) :
        hsv2 = np.zeros((height, width))
     
    
    for r in range(0,height,  windowsize_r):
        for c in range(0,width,  windowsize_c):
                img=normalizacao(img_m[m],u0,v0)
                hsv2[r:r+ windowsize_r , c:c+ windowsize_c]= img
                m=m+1
    return img'''