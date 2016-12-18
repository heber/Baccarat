# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:21:16 2016

@author: shaohb
"""

from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt

img=np.array(Image.open('../pic/bjl.bmp'))  

print img.shape  

im = Image.open('../pic/bjl.bmp')
im2 = Image.new("RGB",im.size,(0,0,0))
#im2.show()

#for x in range(im.size[1]):
#    for y in range(im.size[0]):
#        pix = im.getpixel((y,x))
#        if pix == (255,255,255): # these are the numbers to get
#            im2.putpixel((y,x),(255,255,255))
#            
#im2.show()


white_rows = []

for x in range(im.size[1]):
    num = 0
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == (255,255,255):
            num += 1
    if(num >= im.size[0]/5):
            white_rows.append(x)
            

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

for index in range(len(new_white_rows)):
    for row in range(new_white_rows[index], end_white_rows[index]):
        for y in range(im.size[0]):
            im2.putpixel((y,row), (255,255,255))
            
#im2.show()

first_row = new_white_rows[1]

white_cols = []

for y in range(im.size[0]):
    num = 0
    for x in range(im.size[1]):
        if x < first_row:
            continue
        pix = im.getpixel((y,x))
        if pix == (255,255,255):
            num += 1
    if(num >= (im.size[1] - first_row)/3):
        white_cols.append(y)
        
new_white_cols = []
end_white_cols = []

for j in range(len(white_cols)):
    if(j == 0):
        new_white_cols.append(white_cols[j])
        continue
    elif(j == len(white_cols) -1):
        end_white_cols.append(white_cols[j])
    elif(white_cols[j] != white_cols[j-1] +1):
        new_white_cols.append(white_cols[j])
        end_white_cols.append(white_cols[j-1])

for index in range(len(new_white_cols)):
    for col in range(new_white_cols[index], end_white_cols[index]):
        for x in range(im.size[1]):
            im2.putpixel((col, x), (255,255,255))
            

def find_color(img, lefttop, rightdown):
    middle_row = (lefttop[1] + rightdown[1]) /2
    num = 0
    print "middle_row " + str(middle_row)
    for col in range(lefttop[0], rightdown[0]+1):
        pix = img.getpixel((col, middle_row))
        print pix
        if(pix == (255,0,0)):
            num += 1
            print "find"
            
def all_color(img, lefttop, rightdown):
    for row in range(lefttop[1], rightdown[1] +1):
        print "row " + str(row)
        num = 0
        for col in range(lefttop[0], rightdown[0]+1):
            pix = img.getpixel((col, row))
            print pix
            if(pix == (255,0,0)):
                num += 1
                print "find"

lefttop = (new_white_cols[1], new_white_rows[1])
rightdown = (end_white_cols[1], end_white_rows[1])

all_color(im, lefttop, rightdown)

find_color(im, lefttop, rightdown)

im2.show()