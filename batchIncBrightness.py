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

def adjustImage(infile):
    im = Image.open(infile)
    for f in range(40, 20, -1):
        factor = f / 20.0;
        outfile = os.path.splitext(infile)[0] + ('-%f.png' % factor)
        enhancer = ImageEnhance.Brightness(im)
        tmp = enhancer.enhance(factor)
        enhancer = ImageEnhance.Contrast(tmp)
        tmp = enhancer.enhance(1.15)
        enhancer = ImageEnhance.Color(tmp)
        enhancer.enhance(1.15).save(outfile)

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
