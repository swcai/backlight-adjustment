#!/usr/bin/env python
# file: lumiAdjust.py
# desc: Implementation of a set of Luminance Adjustment Algorithm
#


import os
import sys
import Image
import ImageEnhance

from pprint import pprint


luminanceOfBacklightLevel = [0.3, 0.34, 0.36, 0.38, 0.40, 0.42, 0.45]
backlightLevel = len(luminanceOfBacklightLevel)
kernel = [0, -1, 0, -1, 5, -1, 0, -1, 0]


'''
def balanceContrast(data, width, height):
   sk = sum(kernel)
   for y in range(1, height-1):
      for x in range(1, width-1):
         p = []
         for j in (-1, 0, 1):
            for i in (-1, 0, 1):
               p.append(data[(y+j)*width + (x+i)][0])
         v = 0.0
         for l in range(len(p)):
            v += p[l] * kernel[l]
         t = data[x+y*width]
         data[x+y*width] = (v / sk, t[1], t[2])
''' 


#
# There are some clippings in highlight and lowlight area, with this 
# algorithm. And this gets black to be gray
#
def convert_algo0(y):
   #
   # deltaL = 1.0 - L' / L
   # where L' is the backlight luminance in the new backlight level
   #       L is the backlight luminance in the origin backlight level 
   # L and L' should be a measured value
   #
   deltaL = 1.0 - 0.90 / 1.0
   return int(255 * (min(1.0, y / 255.0 + detlaL)))


#
# There are some clippings with this algorithm
# But this does not make black be gray.
#
def convert_algo1(y):
   #
   # ratio = L / L'
   # where L' is the backlight luminance in the new backlight level
   #       L is the backlight luminance in the origin backlight level 
   # L and L' should be a measured value
   # 
   ratio = 1.0 / .9
   return min(255, int(y * ratio))

#
# Gamma correction
# Need time to find the right function f(L, L') -> gamma value
#
def convert_algo2(y):
   ratio = 0.8 / 1.0
   return int(255.0 * pow(y / 255.0, ratio))


def adjustImage(infile):
    im = Image.open(infile).convert("YCbCr")
    converted = [(convert_algo2(y), cb, cr) for y, cb, cr in im.getdata()]
    im.putdata(converted)
    im = im.convert("RGBA")

    #
    # enhance the new image by contrast
    # 1.1 is a testing data, getting by guess
    #
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(1.1)
    outfile = os.path.splitext(infile)[0] + '.png'
    im.save(outfile)


def usage():
    print "Usage: %s file1" % sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit
    try:
        adjustImage(sys.argv[1])
    except IOError:
        print 'cannot convert', infile
