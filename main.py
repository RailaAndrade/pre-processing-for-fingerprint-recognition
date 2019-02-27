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
import normalizacao
import frequencia
#import filtro_media
'''
#recebe a imagem 
imgteste=cv2.imread('images/DB1_B/110_1.tif',cv2.IMREAD_GRAYSCALE)

#printa a imagem original 
plt.imshow(imgteste, cmap='gray')
plt.figure()

img2=imgteste

hsv = np.zeros((480, 640))
hsv[:,:] = cv2.normalize(imgteste.astype('float'),None,0,1,cv2.NORM_MINMAX)
x = np.zeros((480, 640))
teste=janelamento.janelamento(hsv,20,20)
x=normalizacao.normalizacao(hsv,0.9,0.6)
plt.figure()
plt.imshow(x, cmap='gray',clim=(0,1))
angles = orientacao.orientacao_grad(x,9)
orientacao.desenha_linhas(x,angles,9)
plt.figure()
f=frequencia.freq(angles,hsv, 9,3,10)
fm = janelamento.montar(f,480,640)
plt.imshow(fm, cmap='gray',clim=(0,1))
plt.figure()
f2=frequencia.freq_fft(hsv,9)
ty,tx =f2[0].shape
fm2 = janelamento.montar(f2,480,640)
plt.imshow(fm2, cmap='gray',clim=(0,1))
plt.figure()
oi1=frequencia.freq_map(f2,9)
oi=janelamento.montar(oi1,480,640)
plt.imshow(oi, cmap='gray',clim=(0,1))

plt.show()

'''

#testejanelamento 
#img=cv2.imread('images/DB1_B/101_1.tif',cv2.IMREAD_GRAYSCALE)
img=cv2.imread('images/DB4_B/109_7.tif',cv2.IMREAD_GRAYSCALE)
#img=cv2.imread('images/DB1_B/101_1.tif',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray')




print(normalizacao.calcvar(img))
'''
if normalizacao.calcvar(img)<1416:
    kernel = np.array(( [[-1, -1, -1 ,-1 ,-1],[-1, 2, 2 ,2 ,-1],[-1, 2, 3, 2, -1],[-1, 2, 2 ,2 ,-1],[-1, -1, -1 ,-1 ,-1] ]),dtype="int")*1/3
    img= cv2.filter2D(img,-1,kernel)
'''


img=img.astype(np.float)


#img= cv2.normalize(img, img.astype(np.float), 0,1, cv2.NORM_MINMAX,-1)


height, width = img.shape
img=normalizacao.norm(img)
img=cv2.GaussianBlur(img,(5,5),0)
plt.figure()
janelas=janelamento.janelamento(img,20,20)
janelas_montadas=janelamento.montar(janelas,height,width)



x1=normalizacao.normalizacao(img,1,1)
plt.imshow(x1, cmap='gray',clim=(0,1))





plt.figure()
x=normalizacao.montar_normalizacao(janelas,height,width,1,1)
#x=cv2.GaussianBlur(x,(5,5),0)
plt.imshow(x, cmap='gray',clim=(0,1))





# ORIENTACAO NA IMAGEM NORMALIZADA JANELADA

angles = orientacao.orientacao_grad(x,17)
orientacao.desenha_linhas(x,angles,17)

angles2 = orientacao.orientacao_grad(x,9)
orientacao.desenha_linhas(x,angles2,9)


# ORIENTACAO NA IMAGEM NORMALIZADA COMUM

angles3 = orientacao.orientacao_grad(x1,17)
orientacao.desenha_linhas(x1,angles3,17)

angles4 = orientacao.orientacao_grad(x1,9)
orientacao.desenha_linhas(x1,angles4,9)



'''
angles2 = orientacao.orientacao_grad(normalizacao.normalizacao(img,0.7,1),17)
orientacao.desenha_linhas(normalizacao.normalizacao(img,0.7,1),angles2,17)

'''




'''janelas2=janelamento.janelamento(x,20,20)
angles3=orientacao.montar_orientacao(janelas2,height,width,10)
orientacao.desenha_linhas(x,angles3,10)'''
'''
angles4 = orientacao.orientacao_grad(x,9)
orientacao.desenha_linhas(normalizacao.normalizacao(img,0.7,1),angles4,9)




#frequencia pela orientacao
plt.figure()

f2=frequencia.freq(angles2, x,17,2,9)
fm2 = janelamento.montar(f2,height,width) 
plt.imshow(fm2, cmap='gray',clim=(0,1))

plt.figure()

f=frequencia.freq(angles4, x, 9,3,6)
fm = janelamento.montar(f,height,width)


#fm = janelamento.montar(f,height,width) 
plt.imshow(fm, cmap='gray',clim=(0,1))




'''

plt.figure()



#frequencia por fft
f2=frequencia.freq_fft(x,17)
fm2 = janelamento.montar(f2,height,width)
oi1=frequencia.freq_map(f2,17)
oi=janelamento.montar(oi1,height,width)
plt.imshow(oi, cmap='gray',clim=(0,1))

plt.figure()
'''
f3=frequencia.freq_fft(x,9)
fm3 = janelamento.montar(f3,height,width)
oi2=frequencia.freq_map(f3,9)
oi2=janelamento.montar(oi2,height,width)
plt.imshow(oi2, cmap='gray',clim=(0,1))
'''


#g_kernel = cv2.getGaborKernel((21, 21), 8.0, angles, 10.0, 0.5, 0, ktype=cv2.CV_32F)

#filtered_img = cv2.filter2D(img, cv2.CV_8UC3, g_kernel)

plt.show()

