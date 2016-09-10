# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:12:42 2016

@author: Nevil Dsouza
"""

### SKELETON FOR SEED ENCRYPTION PROGRAM

def K(i):
    print("inside K",i)
    return i

def F(k,r):
    print("inside F",k,r)
    return r

def seed_encrypt(pt):
    print("inside seed_encrypt with PT=",pt)
        
    # int to binary
    bpt = "{0:b}".format(pt)
    print("binary is ",bpt)
    
    # binary to int
    pt = int(bpt,2)
    print("integer is",pt)
    
    #make bpt 128 bit long
    diff = 128 - len(bpt)
    zeros = '0'*diff
    rev_bpt=bpt[::-1]
    temp = rev_bpt+zeros
    bpt = temp[::-1]
    
    #print(rev_bpt,"\n",temp,"\n",bpt,"\n")
    
    #test 128 bit pt
    #print(int(bpt,2))
    #successful
    
    # divide bpt into L and R
    l=bpt[0:64]
    r=bpt[64:127]
    #print("-1",l,r)
    
    # 15 rounds
    for i in range(15):
        t=r
        r="{0:b}".format(int(l,2)^int(F(K(i),r),2))
        l=t
        #print(i,l,r)
    
    #last round
    l="{0:b}".format(int(l,2)^int(F(K(i),r),2))
    r=r
    #print("15",l,r)
    
    bpt=l+r
    
    
    return int(bpt,2)



### MAIN ENTRY FOR ENCRYPTION

PT="45"

CT=seed_encrypt(int(PT))

print("Encrypted CT=",CT)

### END




