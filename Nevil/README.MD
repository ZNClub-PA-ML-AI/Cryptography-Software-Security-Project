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
