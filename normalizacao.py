import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as mimage
import scipy.misc as misc
import itertools as IT

imgteste=cv2.imread('images/107_7.tif',cv2.IMREAD_GRAYSCALE)
img2=imgteste


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
    if(xi!=0) or (yi!=0):
        img_n= np.zeros((ci, ri))

    else:
        img_n= np.zeros((width, height))

 
    height2, width2 = img_n.shape
    
    for r in range(0,height2, 1):
        for c in range(0,width2, 1):
            if r<height and c<width:
                img_n[r,c]=img[r,c]
            else:
                img_n[r,c]=0.5



    # Crop out the window and calculate the histogram
    for r in range(0,height2, windowsize_r):
        for c in range(0,width2, windowsize_c):
            
            img_w[i]=img_n[r:r+windowsize_r , c:c+windowsize_c]
            i += 1
    return img_w


def sqrt(x):
    return (x ** (1/2) )
def pow2(x):
    return (x ** 2 )

def normbin(img):
    height, width = img.shape
    for r in range(0,height, 1):
        for c in range(0,width,1):
            img2[r,c]= img[r,c]/255
    return img2





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
            soma=soma+(pow2(img[r,c]-u))
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
                img_norm[r,c]=u0+sqrt((pow2(img[r,c]-u))*(v0/v))
            else:
                img_norm[r,c]=u0-sqrt((pow2(img[r,c]-u))*(v0/v))
    return img_norm

            


##plt.imshow(teste[0], cmap='gray',interpolation='bicubic')

##plt.show()
 
plt.figure(1)
plt.imshow(imgteste, cmap='gray')  
#print(imgteste)


plt.figure(2)
d = np.zeros((480, 640))
d[:,:]=cv2.normalize(imgteste.astype('float'),None,0,1,cv2.NORM_MINMAX)
teste=janelamento(d,100,100)



#plt.imshow(teste[6],cmap='gray',interpolation='bicubic')
plt.imshow(teste[34], cmap='gray',clim=(0,1))
#cv2.imshow('janelamento',teste[5])  


#teste2=normalizacao(imgn,0.5,0.7)

plt.figure(3)
#plt.imshow(teste2, cmap='gray')
hsv = np.zeros((480, 640))
hsv[:,:] = cv2.normalize(imgteste.astype('float'),None,0,1,cv2.NORM_MINMAX)
print(hsv)

x = np.zeros((480, 640))
x=normalizacao(hsv,0.7,0.5)

plt.imshow(x, cmap='gray',clim=(0,1))
print(x)



#plt.plot(30, 30, 'rx')

plt.show()

