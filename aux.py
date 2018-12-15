import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl


def sqrt(x):
    return (x ** (1/2) )
    
def pow2(x):
    return (x ** 2 )

def normbin(img):
    height, width = img.shape
    img2= np.zeros((height, width))
    for r in range(0,height, 1):
        for c in range(0,width,1):
            img2[r,c]= img[r,c]/255
    return img2

