# BASE64/DNA ENCODER
## A PYTHON SCRIPT FILE TO ENCODE AND DECODE BASE64/DNA TEXT STRINGS.

Usage: python base64_dna.py

| LANGUAGE | FILENAME      | MD5 Hash                         |
|------    |------         | -------                          |
| python   | base64_dna.py | 8c57e546af45fbc7f8cedcde843167fc |

### DNA ENCRYPTION ALGORITHM
------------------------
A cryptographic technique in which each letter of the alphabet is converted into a different combination of the four bases A, C, T, G that make up the human deoxyribonucleic acid (DNA).

Step 1: Convert each ASCII value to its 8-bit binary value.</br>
Step 2: Convert each binary value to an A, C, T, G combination using mapping - 00:A, 01:C, 10:G, and 11:T.</br>
Step 3: Construct a random table that represent all 256 different possible quartet combinations of A, C, T, G (4^4 = 256 = the number of Extended ASCII characters). Use this substitution table to convert each 'ACTG' quartet to an Extended ASCII character (this then forms the encrypted message).

### CONSOLE DISPLAY
![Screenshot](picture1.png)

EXAMPLE: BOY
************
ASCII values of B=66, O=79, Y=89

1. ASCII to binary conversion:</br>
                  B to binary is 01000010</br>
                  O to binary is 01001111</br>
                  Y to binary is 01011001</br>
                  
2. 01000010 => 01=C, 00=A, 00=A, 10=G</br>
   01001111 => 01=C, 00=A, 11=T, 11=T</br>
   01011001 => 01=C, 01=C, 10=G, 01=C</br>
   
   This means it will become CAAG, CATT, CCGC
   
3. Now let's say that in the 256 random combinations table:</br>
   ......
   Position 53: CAAG</br>
   ......
   Position 67: CATT</br>
   ......
   Position 89: CCGC</br>
   
   The encrypted message 'CAAG' becomes '53' which becomes '5' etc.
