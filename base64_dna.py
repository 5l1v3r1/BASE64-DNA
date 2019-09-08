#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#  A SIMPLE PYTHON SCRIPT FILE FOR ENCODING AND DECODING DNA-BASED ENCRYPTED STRINGS
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import random
import base64
import itertools
import linecache

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display my universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print " ____    _    ____  _____ __   _  _        __  ____  _   _    _       _____ _   _  ____ ___  ____  _____ ____   "
print "| __ )  / \  / ___|| ____/ /_ | || |      / / |  _ \| \ | |  / \     | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "|  _ \ / _ \ \___ \|  _|| '_ \| || |_    / /  | | | |  \| | / _ \    |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| |_) / ___ \ ___) | |__| (_) |__   _|  / /   | |_| | |\  |/ ___ \   | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print "|____/_/   \_\____/|_____\___/   |_|   /_/    |____/|_| \_/_/   \_\  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                                                "
print "                             BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                            \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

plainText  = "Blessent mon coeur d'une langueur monotone"
bits2base = {"00":"A", "01":"C", "10":"G", "11":"T"}
base2bits = {"A":"00", "C":"01", "G":"10", "T":"11"}

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

def encrypt(plainText, bits2base):

# ------------------------------------------------------------------------------------- 
# Method  : 1. Convert 8-bit binary values to ASCII values
#         : 2. Convert quartet combinations to binary by mapping A:00 C:01 G:10 T:11
#         : 3. Convert ASCII to A,C,T,G quartet-combinations via the substitution table
# -------------------------------------------------------------------------------------
   
   table = [''.join(x) for x in itertools.product('ATCG', repeat=4)]
   random.shuffle(table)
   assert(len(table)==256)           
   with open('key.txt', 'wt') as f:				# Create unique Key
      for x in table:
         f.write(x)   
   dnaCode   = ""
   encrypted = ""
   for ch in plainText:
      binary = '{0:08b}'.format(ord(ch))
      bit_pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
      base_quartet = ""
      for x in bit_pairs:
         base_quartet += bits2base[x]
         dnaCode = dnaCode + base_quartet
      encrypted = encrypted + chr(table.index(base_quartet))
   return base64.b64encode(encrypted)

def decrypt(encrypted, base2bits):

# ------------------------------------------------------------------------------------- 
# Method  : 1. Convert ASCII to A,C,T,G quartet-combinations via the substitution table
#         : 2. Convert quartet combinations to binary by mapping A:00 C:01 G:10 T:11
#         : 3. Convert 8-bit binary values to ASCII values - forms decrypted message
# -------------------------------------------------------------------------------------

   encrypted = base64.b64decode(encrypted)

   table = []
   with open('key.txt', 'rt') as f:				# Get unique key
      seq = f.read()
      for quartet in [seq[i:i+4] for i in range(0, len(seq), 4)]:
          table.append(quartet)
      assert(len(table)==256)
   decrypted = ""			
   for byte in encrypted:
      base_quartet = table[ord(byte)]
      binary = ""
      for base in base_quartet:
         binary += base2bits[base]
      decrypted = decrypted + chr(int(binary, 2))
   return decrypted

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Encrypt and decrypt plainText.
# Modified: N/A
# -------------------------------------------------------------------------------------

encrypted = encrypt(plainText, bits2base) 	# Creates Key and encrypts plainText.
decrypted = decrypt(encrypted, base2bits)
Key = linecache.getline('key.txt', 1)           # Grab a copy of the key.

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Display program variables and results.
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text : " + plainText
print "DNA Key    : " + Key[:100] + "...\n"
print "Encrypted  : " + encrypted 
print "Decrypted  : " + decrypted + "\n"






