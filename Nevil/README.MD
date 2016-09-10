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

      Z3 = SS0(X0)
      
      Z2 = SS1(X1)
      
      Z1 = SS2(X2)
      
      Z0 = SS3(X3)
      
      SS0(X0)= {S0(X0)& m3} || {S0(X0)& m2} || {S0(X0)& m1} || {S0(X0)& m0}
      
      SS1(X1)= {S1(X1)& m0} || {S1(X1)& m3} || {S1(X1)& m2} || {S1(X1)& m1}
      
      SS2(X2)= {S0(X2)& m1} || {S0(X2)& m0} || {S0(X2)& m3} || {S0(X2)& m2}
      
      SS3(X3)= {S1(X3)& m2} || {S1(X3)& m1} || {S1(X3)& m0} || {S1(X3)& m3}
      
      where,
      
      where m0 = 0xFC, m1 = 0xF3, m2 = 0xCF, and m3 = 0x3F.
  
  The 2 S-boxes & 4 SS-boxes values are given [here](https://tools.ietf.org/html/rfc4269#appendix-A.2)
  
  
### Key Schedule Ki

1. The key schedule generates each round's subkeys.
2. t uses the function G, addition in modular 2**32, subtraction in modular 2**32, and (left/right) circular rotation.
3. A 128-bit input key is divided into four 32-bit blocks (Key0, Key1, Key2, Key3).
4. The two 32-bit subkeys of the ith round, Ki0 and Ki1, are generated as follows:
      1. Type 1 : Odd round
        Ki0 = G(Key0 + Key2 - KCi)
        Ki1 = G(Key1 - Key3 + KCi)
        Key0 || Key1 = (Key0 || Key1) >> 8

      2. Type 2 : Even round
        Ki0 = G(Key0 + Key2 - KCi)
        Ki1 = G(Key1 - Key3 + KCi)
        Key2 || Key3 = (Key2 || Key3) << 8

Where Ki0 is the most significant 32 bits of Ki, and Ki1 is the least
   significant 32 bits of Ki (where i=0,...,3).

   The following table shows constants used in KCi:

          i    |    Value          i    |    Value
         ============================================
         KC1   |  0x9E3779B9      KC2   |  0x3C6EF373
         KC3   |  0x78DDE6E6      KC4   |  0xF1BBCDCC
         KC5   |  0xE3779B99      KC6   |  0xC6EF3733
         KC7   |  0x8DDE6E67      KC8   |  0x1BBCDCCF
         KC9   |  0x3779B99E      KC10  |  0x6EF3733C
         KC11  |  0xDDE6E678      KC12  |  0xBBCDCCF1
         KC13  |  0x779B99E3      KC14  |  0xEF3733C6
         KC15  |  0xDE6E678D      KC16  |  0xBCDCCF1B

   A pseudo code for the key schedule is as follows:

         Input : (Key0, Key1, Key2, Key3)

         for i = 1 to 16
           Ki0 = G(Key0 + Key2 - KCi)
           Ki1 = G(Key1 - Key3 + KCi)
           if i is odd
                  Key0 || Key1 = (Key0 || Key1) >> 8
           else
                  Key2 || Key3 = (Key2 || Key3) << 8

         Output : (Keyi0, Keyi1), i=1 to 16

