import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
import aux
import numpy as np
import janelamento
def freq(teta,img,n, minWaveLength, maxWaveLength):
    scos=0.0
    waveLength=0
    ssin=0.0
    imgw={}
    l=0
    freqim = np.ones((n,n))

    
    
    end=0
    blockh=n
    height, width = img.shape
    for r in range(0,height,n):
    
        for c in range(0,width,n):

            teta2 = 2*teta[r,c] 
            scos=scos+math.cos(teta2)
            ssin=ssin+math.sin(teta2)
            cosorient=scos/(n*2*n)

            sinorient = ssin/(n*2*n) 
            orient = math.atan2(sinorient,cosorient)/2
            M = cv2.getRotationMatrix2D((r//2,c//2),orient,1)
            #print(M)
            p=int(r/2)
            q=int(c/2)
            if c>n and r>n:
                #dst= cv2.warpAffine(img[r:r+n, c:c+n],M,(p,q))
                dst= cv2.warpAffine(img[r-(n//2):r+(n//2), c-n:c+n],M,(r,c))
                
            else:
                dst= cv2.warpAffine(img[r:r+n, c:c+n],M,(p,q))
                #dst= cv2.warpAffine(img[r:r+(n//2), c:c+n],M,(p,q))

                

        

            #cropsze = math.ceil(n/aux.sqrt(2))
            #offset = math.ceil((n-cropsze)/2)                
            proj = sum(dst)
            kernel= np.ones((n,1))
            dilation = cv2.dilate(proj,kernel,1)
            x = len(dilation)
            
            maxpts=[]
            projm=np.mean(proj)
            maxind=[]

              
            for i in range(0,x):
                if (dilation[i] == proj[i]) and (proj[i] > projm):
                    maxpts.append(1)
                    #print (dilation)   
                    maxind.append(i)
                    
                else:
                    maxpts.append(0)
                 
            
              
            if len(maxind) < 1:
                freqim = np.zeros((n,n))
            else:
                NoOfPeaks = len(maxind)
                #print(maxind)
                #if (maxind[-1]!=0) and (maxind[0]!=0) :
                waveLength = (maxind[-1]- maxind[0])/(NoOfPeaks)
                #else: 
                #    waveLength=0
                
            if (waveLength > minWaveLength) and (waveLength < maxWaveLength) :
                freqim = 1/waveLength * np.ones((n,n))
                
               
            else:
                freqim = np.zeros((n,n))
            imgw[l]=freqim   
            l+=1
            
    return imgw

def freq_fft(img,n):
    
    l=0
    
    imgw=janelamento.janelamento(img,n,n)
    height, width = imgw[0].shape
    for l in range(0,len(imgw)):
        img_float32 = np.float32(imgw[l])
       
        dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
        dft_shift= np.fft.fftshift(dft)
        imgw[l]= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
        #plt.imshow(imgw, cmap = 'gray')
        
    '''
    for r in range(0,height,n):
        for c in range(0,width,n):
            img_float32 = np.float32(img[r:r+(n//2),c:c+n])
            imgw[l]=np.zeros((n,n))
            dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
            dft_shift= np.fft.fftshift(dft)
            imgw[l]= 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
            #plt.imshow(imgw, cmap = 'gray')
            l=l+1'''
    return imgw

def freq_map(img,n):
    mapa={}
    maxv=0
    freqb=np.zeros((n,n))
    height,width=img[0].shape
    freqb[:,:]=0.0

    for i in range(0,len(img)):
        temp=img[i]
        maxv=0
        um=0
        vm=0
        ul=0
        vl=0
        for v in range(0,height//2):
            for u in range(0,width):
                if(maxv<abs(temp[v,u]) and abs(temp[v,u])>0.05 and abs(temp[v,u])<0.3):
                    maxv=abs(temp[v,u])
                    vm=v
                    um=u

        #print(vm)
        if um<(n-2) and vm<(n-2):
            if abs(temp[vm,um-1])>abs(temp[vm,um+1]) or um==0:
                vl= vm-(abs(temp[vm,um-1])/(abs(temp[vm,um-1])+abs(temp[vm,um])))
            else:
                vl= vm +(abs(temp[vm,um+1])/(abs(temp[vm,um+1])+abs(temp[vm,um])))
        
            if abs(temp[vm-1,um])>abs(temp[vm+1,um]) or vm==0 :
                ul= um-(abs(temp[vm-1,um])/(abs(temp[vm-1,um])+abs(temp[vm,um])))
            else:
                ul= um +(abs(temp[vm+1,um])/(abs(temp[vm+1,um])+abs(temp[vm,um])))
            
            
  
        
        temp2=aux.sqrt(aux.pow2(ul-(n/2))+aux.pow2(vl-(n/2)))/n
        if math.isnan(temp2):
            freqb[:,:]=0.0
        else:
            freqb[:,:]=temp2
        #print(i)
        #print('i')

        mapa[i]=np.float32(freqb)
       
        #print(mapa[i])
            
    return mapa