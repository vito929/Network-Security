#exercise 1&2
##ecb(electronic code book mode)
1. need to pad and unpad
2. same plaintext reflects to same ciphertext
    - some characteristics can be recongized after encryption
3. modify ciphertext will influence plaintext

##cbc
1. need to pad and unpad
2. same plaintext reflects to different ciphertext only if iv changes everytime
3. modify ciphertext will influence plaintext
4. need feedback

##ctr
1. don't need feedback 
2. parallelization-> fast speed
3. don't need pad any more (because the length of nonce and counter is eaqual to key?)

!!!! all of the above algorithm don't ensure the integrity, that is, above methods allow an adversary to modify the plaintext by performing operations on ciphertext.

##gcm
1. includes ctr mode and MAC(message authentication code)
2. need nonce for ctr mode and tag for authentication
	- use encrypt_and_digest() to encrypt
	- use decrypt_and_verify() to decrypt
3. it will be fail in the process of decryption when the ciphertext is modified.

#exercise 3
1. using xor
2. encry: ciphertext = key ^ plaintext
   decry: plaintext  = key ^ ciphertext
	c = k ^ dk
	I use dk ^ se ^ c to get k ^ se
	then decrypt (k^se^k) to get se

#exercise 5
1. picture has many attributes: data, height,width...
	so since GCM can protect data of the picture, can GCM protect height or width?
2. modify the height and width of the ciphertext and decrypt, we found that the decryption succeeds and height, width of the picture changes.
	
