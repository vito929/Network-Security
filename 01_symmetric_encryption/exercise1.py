# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:07:13 2021

@author: Kwz
"""



from ppmcrypt import *

with open('dk.ppm', 'rb') as f:
        original_image = PPMImage.load_from_file(f)

key = secrets.token_bytes(16)
image=original_image.copy()
image.encrypt(key,'ecb')
#image.write_to_file(open('dk_ecb.ppm', 'wb'))

image.data[42]=0x55
image.decrypt(key)
image.write_to_file(open('dk_ecb_decryp.ppm', 'wb'))
print(key)


##ecb(electronic code book mode)
##1. need to pad and unpad
##2. same plaintext reflects to same ciphertext
##    - some characteristics can be recongized after encryption
