# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:12:42 2016

@author: Nevil Dsouza
"""

### SKELETON FOR SEED ENCRYPTION PROGRAM

def seed_encrypt(pt):
    print("inside seed_encrypt with PT=",pt)
        
    # int to binary
    bpt = "{0:b}".format(pt)
    print("binary is ",bpt)
    
    # binary to int
    pt = int(bpt,2)
    print("integer is",pt)
    
    #make bpt 128 bit long
    
    
    return bpt



### MAIN ENTRY FOR ENCRYPTION

PT="45"

CT=seed_encrypt(int(PT))

print("Encrypted CT=",CT)

### END




