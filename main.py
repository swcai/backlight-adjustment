#!/usr/bin/env python
# file: main.py
# desc: handy PIL script to adjust image for different background
# log:
#          first implementation is over-simplified and used for prototype
#

import os
import sys
import Image
import ImageEnhance
from pprint import pprint

def adjustImage(infile, factor):
    outfile = os.path.splitext(infile)[0] + '-updated.png'
    try:
        im = Image.open(infile)
        width, height = im.size
        print im.size, im.mode
        enhancer = ImageEnhance.Brightness(im)
        enhancer.enhance(factor).save(outfile)
    except:
        raise IOError

def usage():
    print "Usage: %s factor file1 [file2...]" % sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit
    factor = float(sys.argv[1])
    for infile in sys.argv[2:]:
        try:
            adjustImage(infile, factor)
        except IOError:
            print 'cannot convert', infile
