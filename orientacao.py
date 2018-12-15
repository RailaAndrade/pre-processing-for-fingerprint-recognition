import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import aux
import math
from PIL import Image, ImageDraw, ImageFont


def orientacao_grad(img,n):   

    height,width =img.shape  
    Fy = np.zeros((height, width))
    Fx = np.zeros((height, width))
    sobelx= np.zeros((height, width))
    sobely = np.zeros((height, width))
    smoothed = np.zeros((height, width))
    coherence = np.zeros((height, width))
    mapa = np.zeros((height, width))


    fprintWithDirectionsSmoo=np.ones((height, width))
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    sobelxy = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)

    #sobelx = cv2.Scharr(img,cv2.CV_64F,1,0,5)
    #sobely = cv2.Scharr(img,cv2.CV_64F,0,1,5)

    fi=0.0
    
            
           
    for r in range(0,height,n):
    
        for c in range(0,width,n):
            

  
            Gsx=0.0
            Fx_gauss=0.0
            Fy_gauss=0.0
            Gsy=0.0
            Gsu=0.0
            Gxx = 0.0
            Gyy = 0.0
            Gxy=0.0
            coh=0.0
        

            if((height-r)<n):

                blockH = height-r
            else :
                blockH=n
            
            if(width-c)<n:
                blockW = (width-c)
            else:
                blockW=n

            for i in range(r,r+blockH):
                for j in range(c,c+blockW):

                    Gsx +=(sobelx[i,j]*sobelx[i,j]) - (sobely[i,j]*sobely[i,j])
                    Gsy += 2*sobelx[i,j]* sobely[i,j]   
                    Gxy +=sobelx[i,j]*sobely[i,j]   
                    Gxx += sobelx[i,j]*sobelx[i,j]
                    Gyy += sobely[i,j]*sobely[i,j]
                    Gsu +=(sobelx[i,j]*sobelx[i,j]) + (sobely[i,j]*sobely[i,j])
           
           
            if (Gxx + Gyy)==0:
                coh = aux.sqrt(pow(Gsx,2) + pow(Gsy,2)) / 0.1
            else:     
                coh = aux.sqrt(pow(Gsx,2) + pow(Gsy,2)) / Gxx+Gyy
           
            
      
            if (Gxx - Gyy) == 0 and (Gxy == 0):
                fi= 0.0
            elif (Gxx - Gyy) == 0:
                fi = math.pi/2
            else:
                fi = (0.5*math.atan2(Gsy, Gsx))

            if fi< 0.0:
                fi = fi +2*math.pi


            
           
            Fx[r,c] =math.cos(2*fi)
            Fy[r,c]= math.sin(2*fi)

            mapa[r,c] = fi


            #Fx=cv2.normalize(Fx.astype('float'),None,0,1,cv2.NORM_MINMAX)
            #Fy=cv2.normalize(Fy.astype('float'),None,0,1,cv2.NORM_MINMAX)
            for u in range(r,r+blockH):
        
                for v in range( c,c+blockW):
                    Fx[u,v] =  Fx[r,c]
                    Fy[u,v] =  Fy[r,c]
                    
                    if coh<0.75:
                        coherence[u,v]=1
                    else:
                        coherence[u,v]=0
    
    Fx_gauss = cv2.GaussianBlur(Fx, (5, 5), 0)
    Fy_gauss = cv2.GaussianBlur(Fy, (5, 5), 0)

    for r in range(0,height):
        for c in range(0,width):
            smoothed[r,c]= (0.5*math.atan2(Fy_gauss[r,c], Fx_gauss[r,c]))
           
            '''if r%n==0 and c%n ==0:
                x = c
                y = r

                length =n

                y2 = int(y - length * math.cos(smoothed[r,c]))
                x2 = int(x + length * math.sin(smoothed[r,c]))
           

                plt.plot([x, x2], [y, y2], 'b-', linewidth=1.5)
                plt.plot([x,x], [y, y+n], 'k-', linewidth=0.5)
                plt.plot([x, x+n], [y, y], 'k-', linewidth=0.5)

                #cv2.line(fprintWithDirectionsSmoo,(y, x), (y2, x2), 0, 1, 1)
                #cv2.line(fprintWithDirectionsSmoo,(x, y), (x,y+n),(0,255,0),1 ,8,0)
                #cv2.line(fprintWithDirectionsSmoo,(x, y), (x+n,y),(0,255,0),1 ,8,0)'''
                



        
    return smoothed

def desenha_linhas(img,teta,n):   
    
    plt.figure()
    height,width =img.shape  
    for r in range(0,height):
        for c in range(0,width):
            if r%n==0 and c%n ==0:
                x = c
                y = r

                length =n

                y2 = int(y - length * math.cos(teta[r,c]))
                x2 = int(x + length * math.sin(teta[r,c]))
           

                plt.plot([x, x2], [y, y2], 'b-', linewidth=1.5)
                plt.plot([x,x], [y, y+n], 'k-', linewidth=0.5)
                plt.plot([x, x+n], [y, y], 'k-', linewidth=0.5)
    plt.imshow(img, cmap='gray',clim=(0,1))
    ##plt.figure()
    ##plt.imshow(teta, cmap='gray',clim=(0,1))

    


