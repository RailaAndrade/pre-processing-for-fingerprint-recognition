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


imgteste=cv2.imread('images/101_1.tif',cv2.IMREAD_GRAYSCALE)
img2=imgteste





'''

plt.figure(1)
plt.imshow(imgteste, cmap='gray')  '''
#print(imgteste)


#plt.figure(2)



#plt.subplot(1,6,1),plt.imshow(teste[1],cmap = 'gray')
#plt.title(''), plt.xticks([]), plt.yticks([])







hsv = np.zeros((480, 640))
hsv[:,:] = cv2.normalize(imgteste.astype('float'),None,0,1,cv2.NORM_MINMAX)


x = np.zeros((480, 640))

#teste=janelamento(hsv,20,20)

x=normalizacao.normalizacao(hsv,0.7,0.5)
plt.figure()
plt.imshow(x, cmap='gray',clim=(0,1))

angles = orientacao.orientacao_grad(x,17)

orientacao.desenha_linhas(hsv,angles,17)

#angles = calculate_angles(x, 10, f, g)
#draw_lines(hsv, angles, 10).show()









#plt.plot(30, 30, 'rx')

'''
plt.figure(3)
d = np.zeros((480, 640))
d[:,:]=cv2.normalize(imgteste.astype('float'),None,0,1,cv2.NORM_MINMAX)
teste=janelamento.janelamento(d,20,20)

hsv2 = janelamento.montar(teste,480,640)


plt.imshow(hsv2, cmap='gray',clim=(0,1))'''

plt.figure()
f=frequencia.freq(angles,hsv, 17,3,15)
fm = janelamento.montar(f,480,640)
plt.imshow(fm, cmap='gray',clim=(0,1))
plt.show()


