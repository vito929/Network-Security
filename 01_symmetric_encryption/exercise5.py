# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:07:13 2021

@author: Kwz
"""



from ppmcrypt import *

with open('security.ppm', 'rb') as f:
        original_dk = PPMImage.load_from_file(f)

        

key = secrets.token_bytes(16)
##--------------------- ctr
image_dk=original_dk.copy()

image_dk.encrypt(key,'gcm')
image_dk.write_to_file(open('security_gcm.ppm', 'wb'))

image_dk.height=245
image_dk.width=480
image_dk.decrypt(key)
image_dk.write_to_file(open('security_gcm_decrypt.ppm', 'wb'))


