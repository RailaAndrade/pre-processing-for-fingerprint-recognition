import math
import cv2
import aux
import numpy as np
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
            M = cv2.getRotationMatrix2D((r/2,c/2),orient,1)
            p=int(r/2)
            q=int(c/2)
            dst= cv2.warpAffine(img[r:r+n, c:c+n+n],M,(p,q))
            
            

            #cropsze = math.ceil(n/aux.sqrt(2))
            #offset = math.ceil((n-cropsze)/2)                
            proj = sum(dst)
            kernel= np.ones((n,1))
            dilation = cv2.dilate(proj,kernel,iterations = 1)
            
            maxind=0
            


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
                 
            
              
            if len(maxind) < 2:
                freqim = np.zeros((n,n))
            else:
                NoOfPeaks = len(maxind)
                #print(maxind)
                if (maxind[-1]!=0) and (maxind[0]!=0) :
                    waveLength = (maxind[-1]- maxind[0])/(NoOfPeaks-1)
                else: 
                    waveLength=0
                
            if (waveLength > minWaveLength) and (waveLength < maxWaveLength) :
                freqim = 1/waveLength * np.ones((n,n))
            else:
                freqim = np.zeros((n,n))
            imgw[l]=freqim   
            l+=1
    return imgw


    #dst = dst[offset:offset+cropsze, offset:offset+cropsze]
    '''kernel= np.ones((1,n))
    dilation = cv2.dilate(proj,kernel,iterations = 1)
    print(dilation)
    print('jjj')
    print(proj)
    maxpts= np.ones((n,1))
    ind= np.ones((n,1))
    y,x = dilation.shape
    for j in range(0,y):
        for i in range(0,x):
            if (dilation[j,i] == proj[j]) and (proj[j] > np.mean(proj)):
                maxpts[j]=dilation[j,i] 
                ind[j]=j
                maxind=maxind+1
            else:
                maxpts[j]=0
                ind[j]=0
    if  maxind < 2:
	    freqim = np.zeros((height,width))
    else:
        NoOfPeaks = maxind
        if (ind[maxind]!=0) and (ind[1]!=0) :
	        waveLength = (ind[maxind]-ind[1]/(NoOfPeaks-1))
        else: 
            waveLength=0
        
    if (waveLength > minWaveLength) and (waveLength < maxWaveLength) :
	    freqim = 1/waveLength * np.ones((height,width))
    else:
	    freqim = np.zeros((height,width))'''

    


'''def freq(teta,img,block_size, minWaveLength, maxWaveLength):
    height, width = img.shape

    scos=0.0
    ssin=0.0
    maxind=0
longitude = np.zeros(2,width)


    for r in range(0,height):
        for c in range(0,width):
            #teta2 = 2*teta[r,c] 
            teta2=math.pi/2+teta[r,c]
            scos=scos+math.cos(teta2)
            ssin=ssin+math.sin(teta2)
            

    cosorient=scos/(height*width)

    sinorient = ssin/(height*width) 
    orient = math.atan2(sinorient,cosorient)/2
    
    M = cv2.getRotationMatrix2D((width/2,height/2),orient,1)
    dst = cv2.warpAffine(img,M,(width,height)) 

    cropsze = math.ceil(height/aux.sqrt(2))
    offset = math.ceil((height-cropsze)/2)
    dst = dst[offset:offset+cropsze, offset:offset+cropsze];   
    proj = sum(M)
    kernel= np.ones((1,n))
    dilation = cv2.dilate(proj,kernel,iterations = 1)
    print(dilation)
    print('jjj')
    print(proj)
    maxpts= np.ones((n,1))
    ind= np.ones((n,1))
    y,x = dilation.shape
    for j in range(0,y):
        for i in range(0,x):
            if (dilation[j,i] == proj[j]) and (proj[j] > np.mean(proj)):
                maxpts[j]=dilation[j,i] 
                ind[j]=j
                maxind=maxind+1
            else:
                maxpts[j]=0
                ind[j]=0
    if  maxind < 2:
	    freqim = np.zeros((height,width))
    else:
        NoOfPeaks = maxind
        if (ind[maxind]!=0) and (ind[1]!=0) :
	        waveLength = (ind[maxind]-ind[1]/(NoOfPeaks-1))
        else: 
            waveLength=0
        
    if (waveLength > minWaveLength) and (waveLength < maxWaveLength) :
	    freqim = 1/waveLength * np.ones((height,width))
    else:
	    freqim = np.zeros((height,width))

    return'''