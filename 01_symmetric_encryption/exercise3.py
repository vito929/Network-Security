# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:07:13 2021

@author: Kwz
"""



from ppmcrypt import *

with open('dk.ppm', 'rb') as f:
        original_dk = PPMImage.load_from_file(f)
with open('se.ppm', 'rb') as g:
        original_se = PPMImage.load_from_file(g)
        
def xor(xs, ys):
    """Compute the bit-wise xor of two byte-like objects."""
    return bytes(x ^ y for x, y in zip(xs, ys))

key = secrets.token_bytes(16)
##--------------------- ctr
image_dk=original_dk.copy()
image_se=original_se.copy()
assert len(image_dk.data) == len(image_se.data)
image_dk.encrypt(key,'ctr')

diff=xor(original_dk.data,original_se.data)
image_dk.data=xor(diff,image_dk.data)

image_dk.decrypt(key)
image_dk.write_to_file(open('exercise3.ppm', 'wb'))


