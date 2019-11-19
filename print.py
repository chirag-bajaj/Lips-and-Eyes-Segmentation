import cv2
import matplotlib.pyplot as plt
path='/test_out/images/'
for i in range(1,6):
    img=cv2.imread(path+str(i)+'-inputs.png')
    mask=cv2.imread(path+str(i)+'-outputs.png')
    la=cv2.addWeighted(src1=img, alpha=0.5, src2=mask, beta=0.5 , gamma=0.0)
    fig=plt.figure()
    a = fig.add_subplot(1,3,1)
    imgplot = plt.imshow(img)
    a.set_title('Input')
    a = fig.add_subplot(1,3,2)
    imgplot = plt.imshow(mask)
    a.set_title('Output')
    a = fig.add_subplot(1,3,3)
    imgplot = plt.imshow(la)
    a.set_title('Output')
'''    
im=cv2.imread('im.png')
ma=cv2.imread('ma.png')
cv2.imshow('out',im)
        
cv2.imshow('outi',ma)
la=cv2.addWeighted(src1=im, alpha=0.5, src2=ma, beta=0.5 , gamma=0.0)
cv2.imshow('outs',la)
'''
