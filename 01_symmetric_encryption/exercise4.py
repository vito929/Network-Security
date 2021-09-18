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
        

key = secrets.token_bytes(16)
##--------------------- ctr
image_dk=original_dk.copy()
image_se=original_se.copy()

image_dk.encrypt(key,'gcm')
image_dk.write_to_file(open('dk_gcm.ppm', 'wb'))

image_dk.data[42]=0x55
image_dk.decrypt(key)
image_dk.write_to_file(open('dk_gcm_decrypt.ppm', 'wb'))


