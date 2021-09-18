# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:07:13 2021

@author: Kwz
"""



from ppmcrypt import *

with open('tux.ppm', 'rb') as f:
        original_image = PPMImage.load_from_file(f)

key = secrets.token_bytes(16)
print(key)
#--------------------- cbc
##image=original_image.copy()
##image.encrypt(key,'cbc')
##image.write_to_file(open('dk_cbc.ppm', 'wb'))
##
##
##image.data[42]=0x55
##image.decrypt(key)
##image.write_to_file(open('dk_cbc_decryp.ppm', 'wb'))
##print(key)

##--------------------- ctr
image=original_image.copy()
image.encrypt(key,'ctr')
print(key)
image.write_to_file(open('tux_ctr.ppm', 'wb'))


image.data[42]=0x55
image.decrypt(key)
image.write_to_file(open('dtux_ctr_decryp.ppm', 'wb'))
print(key)

