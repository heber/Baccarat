# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:21:16 2016

@author: shaoh
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=np.array(Image.open('d:/bjl.bmp'))  #打开图像并转化为数字矩阵
plt.figure("BJL")
plt.imshow(img)
plt.axis('off')
#plt.show()

print img.shape  
#print img.dtype 
#print img.size 
#print type(img)

white_rows = []

rows,cols,colors=img.shape
for i in range(rows):
    num = 0
    for j in range(cols):
        if (img[i,j,0]==255 and img[i,j,1]==255 and img[i,j,2]==255):
            num += 1
    if(num >= cols/5):
        #img[i,]=255
        #print i
        white_rows.append(i)

#plt.imshow(img)

new_white_rows = []
end_white_rows = []

for i in range(len(white_rows)):
    if(i ==0):
        new_white_rows.append(white_rows[i])
        continue
    elif(i == len(white_rows)-1):
        end_white_rows.append(white_rows[i])
    elif(white_rows[i] != white_rows[i-1] +1):
        new_white_rows.append( white_rows[i])
        end_white_rows.append( white_rows[i-1])

print len(new_white_rows)
print new_white_rows
print end_white_rows
        
white_cols =[]

for j in range(cols):
    num = 0
    for i in range(rows):
        if (img[i,j,0]==255 and img[i,j,1]==255 and img[i,j,2]==255):
            num += 1
    if(num >= rows/6):
        #img[i,]=255
        #print j
        white_cols.append(j)
        
new_white_cols = []

for i in range(len(white_cols)):
    if(i ==0):
        continue
    elif(white_cols[i] != white_cols[i-1] +1):
        new_white_cols.append( white_cols[i])

big_white_cols = []
for i in range(len(new_white_cols)):
    if(i == 0):
        big_white_cols.append(new_white_cols[i])
        continue
    elif(new_white_cols[i] > new_white_cols[i-1] + 12):
        big_white_cols.append(new_white_cols[i])
    
