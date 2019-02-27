# Cryptography & Software Security Project
1. [Encryption Algorithm Implementation](https://github.com/ZNevzz/CSS-Project/blob/master/README.md#encryption-algorithm)
2. [Research paper presentation](https://github.com/ZNevzz/CSS-Project#research-paper)

## [Encryption Algorithm](https://github.com/ZNevzz/CSS-Project/tree/master/Nevil)

## Research Paper

### [Presentation](https://github.com/ZNevzz/CSS-Project/blob/master/CSS%20Research%20paper-Nevzz.pptx)

### Proposed algorithm

1. Assignment of values:
  1. Letters A,B,..,Z as 1,2,..,26.
  2. Digits 1,2,..,9 as 27,28,..,35.
  3. Digit 0 as 0 only.
2. PT is divided into blocks of 16 bytes represented by Matrix Mp.
3. Key is array K of size 16 which has values generated from random(1,26) with repetition.
4. Perform transpose of Mp as Mp^T
5. Formulate Encrypted Key matrix Ke using for i in Ke: i=i%2
6. Resultant Matrix Cpk = Mp^T + Ke
7. Since Cpk is a 4x4 matrix,
  1. Rotate 1st row by 1 element, 2nd row by 2 elements, 3rd row by 3 elements, 4th row by 0 elements. This gives matrix Chr.
  2. Rotate 1st column by 1 element, 2nd column by 2 elements, 3rd column by 3 elements, 4th column by 0 elements. This gives matrix Cvr.
8. Matrix Cvr is the final encrypted block

