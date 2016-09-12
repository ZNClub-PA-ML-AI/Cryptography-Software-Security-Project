# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:10:39 2016

@author: Nevil Dsouza
"""

### SKELETON FOR SEED ENCRYPTION PROGRAM
def make_64b(bpt):
    diff = 64 - len(bpt)
    zeros = '0'*diff
    rev_bpt=bpt[::-1]
    temp = rev_bpt+zeros
    bpt = temp[::-1]
    return bpt



def make_128b(bpt):
    diff = 128 - len(bpt)
    zeros = '0'*diff
    rev_bpt=bpt[::-1]
    temp = rev_bpt+zeros
    bpt = temp[::-1]
    return bpt


def G(x):
    print("inside G",x)
    return x




def K(i):
    print("inside K",i)
    
    # get key
    bkey = "{0:b}".format(int(KEY))
    #print(bkey)
    #print(make_128b(bkey))
    bkey=make_128b(bkey)
    
    # divide 128b key in 4 parts
    key0=bkey[0:31]
    key1=bkey[32:63]
    key2=bkey[64:95]
    key3=bkey[96:127]
    #print(key0,key1,key2,key3)
    gx = int(key0,2)%mod+int(key2,2)%mod-int(kc[i+1],16)%mod
    k0=G(abs(gx))
    #print(k0)
    gx = int(key1,2)%mod-int(key3,2)%mod+int(kc[i+1],16)%mod
    k1=G(abs(gx))
    
    ## odd even based shift
    if (i+1)%2==0:
        temp = key2+key3
        #shift
        ntemp= int(temp,2)
        ntemp= ntemp<<8
        temp = "{0:b}".format(ntemp)
        temp = make_64b(temp)
        #split
        key2=temp[0:31]
        key3=temp[32:63]
        
    else:
        temp = key2+key3
        #shift
        ntemp= int(temp,2)
        ntemp= ntemp>>8
        temp = "{0:b}".format(ntemp)
        temp = make_64b(temp)
        #split
        key2=temp[0:31]
        key3=temp[32:63]
    return (k0,k1)

def F(k,r):
    print("inside F",k,r)
    k0,k1=k
    return r

def seed_encrypt(pt):
    print("inside seed_encrypt with PT=",pt)
        
    # int to binary
    bpt = "{0:b}".format(pt)
#    bpt=bin(pt) # prints 0b101101
    print("binary is ",bpt)
    
    # binary to int
    pt = int(bpt,2)
    print("integer is",pt)
    
    #make bpt 128 bit long
    bpt = make_128b(bpt)
    
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

### global data
kc={1:"0x9E3779B9",2:"0x3C6EF373",3:"0x78DDE6E6",4:"0xF1BBCDCC",
5:"0xE3779B99",6:"0xC6EF3733",7:"0x8DDE6E67",8:"0x1BBCDCCF",
9:"0x3779B99E",10:"0x6EF3733C",11:"0xDDE6E678",12:"0xBBCDCCF1",
13:"0x779B99E3",14:"0xEF3733C6",15:"0xDE6E678D",16:"0xBCDCCF1B"}


mod=4294967296

PT="45"
KEY="7059"
CT=seed_encrypt(int(PT))

print("Encrypted CT=",CT)

### END




