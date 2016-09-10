# SEED algorithm

## Overview

SEED is a 128-bit symmetric key block cipher that has been developed by KISA (Korea Information Security Agency) since 1998. It has the Feistel
structure with 16-round and is strong against DC (Differential Cryptanalysis), LC (Linear Cryptanalysis), and related key attacks, balanced with security/efficiency trade-off. SEED has been widely used in the Republic of Korea for confidential services such as electronic commerce; e.g., financial services provided in wired and wireless communication.


## Features
-  The Feistel structure with 16-round
-  128-bit input/output data block size
-  128-bit key length
-  A round function that is strong against known attacks
-  Two 8x8 S-boxes
-  Mixed operations of XOR and modular addition

## Notations
      &             bitwise AND
      ^             bitwise exclusive OR
      +             addition in modular 2**32
      -             subtraction in modular 2**32
      ||            concatenation
      << n          left circular rotation by n bits
      >> n          right circular rotation by n bits
      0x            hexadecimal representation

## Algorithm

A 128-bit input is divided into two 64-bit blocks (L, R), and the right 64-bit block is an input to the round function F, with a 64-bit subkey Ki generated from the key schedule.  L is the most significant 64 bits of 128-bit input, and R is the least significant 64 bits.

A Fiestel Structure

![wikipedia fiestel structure](https://upload.wikimedia.org/wikipedia/commons/f/fa/Feistel_cipher_diagram_en.svg "16 ROUNDS in SEED ENCRYPTION & DECRYPTION")


### Abstract Skeleton
Input : (L, R)

```python
  for i = 1 to 15

      T = R;
      R = L ^ F(Ki, R);
      L = T;

  L = L ^ F(K16, R), R=R
```
  Output : (L, R)

  Where T is a temporary.

### Function F(Ki,R)


1. A 64-bit input block of the round function F is divided into two 32-bit blocks (R0, R1) and wrapped with 4 phases:
  1. 1 phase of mixing two 32-bit subkey blocks (Ki0, Ki1)
  2. 3 phases of function G(), with additions for mixing two 32-bit blocks.
  3. Output (R0',R1') are as:
    1. R0'= 
            
            G[ <br/>
              G[  
                G[(R0 ^ Ki0) ^ (R1 ^ Ki1)
                ]
                + (R0 ^ Ki0)
              ]
              + 
              G[(R0 ^ Ki0) ^ (R1 ^ Ki1)
              ]
            ] 
            + 
            G[ 
                G[(R0 ^ Ki0) ^ (R1 ^ Ki1)
                ] + (R0 ^ Ki0)
            ]
            
    2. R1'= 
            
                  G[ 
                    G[ 
                      G[(R0 ^ Ki0) ^ (R1 ^ Ki1)
                      ] + (R0 ^ Ki0)
                    ] 
                    + 
                    G[(R0 ^ Ki0) ^(R1 ^ Ki1)
                    ]
                  ]

  
### Function G(X)
1. 32 bit X is divided into 4 sub blocks of 8 bit as X= X3 || X2 || X1 || X0.
2. Output Z is madeup of 4 8-bit sub blocks as Z = Z3 ^ Z2 ^ Z1 ^ Z0.
3. The computation for Zi is as:
      Z3 = SS0
      Z2 = SS1
      Z1 = SS2
      Z0 = SS3

      where,
      SS0(X0)= {S0(X0)& m3} || {S0(X0)& m2} || {S0(X0)& m1} || {S0(X0)& m0}
      SS1(X1)= {S1(X1)& m0} || {S1(X1)& m3} || {S1(X1)& m2} || {S1(X1)& m1}
      SS2(X2)= {S0(X2)& m1} || {S0(X2)& m0} || {S0(X2)& m3} || {S0(X2)& m2}
      SS3(X3)= {S1(X3)& m2} || {S1(X3)& m1} || {S1(X3)& m0} || {S1(X3)& m3}
      
      where
      
