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


imgteste=cv2.imread('images/106_6.tif',cv2.IMREAD_GRAYSCALE)
img2=imgteste

 # ----------------------------------------auxiliares------------------------------------

def soma_nc(img,height,width):

    soma=0
    for r in range(0,height, 1):
        for c in range(0,width, 1):
            soma=soma+img[r,c]
    return soma



def soma_var(img,height,width,u):
    soma=0  
    n=height*width
    for r in range(0,height, 1):
        for c in range(0,width, 1):
            soma=soma+(aux.pow2(img[r,c]-u))
    return soma

def normalizacao(img,u0,v0):
    height, width = img.shape

    #u valor médio da imagem
    
    u=soma_nc(img,height,width)/(height*width)
    #print(u)
    
    #u0 valor médio esperado
    v=soma_var(img,height,width,u)/((height*width)-1)
    #print(v)
    img_norm= np.zeros((height, width))

   
    for r in range(0,height, 1):
        for c in range(0,width, 1):
            if(img[r,c]>u):
                img_norm[r,c]=u0+aux.sqrt((aux.pow2(img[r,c]-u))*(v0/v))
            else:
                img_norm[r,c]=u0-aux.sqrt((aux.pow2(img[r,c]-u))*(v0/v))
    return img_norm
 





