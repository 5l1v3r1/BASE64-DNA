#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#            PYTHON UTILITY FILE TO ENCODE AND DECODE DNA-BASED CRYPTOGRAMS
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import os.path
import random
import itertools
from termcolor import colored	# pip install termcolor

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create a main menu system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

menu = {}
menu['(1)']="Create Secret Message."
menu['(2)']="Encrypt Secret Message."
menu['(3)']="Delete Secret Message."
menu['(4)']="Decrypt Secret Message."
menu['(5)']="Read Secret Message."
menu['(6)']="Clean all files and Exit."

while True: 
   os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------
   print " ____  _   _    _       ____ ______   ______ _____ ___   ____ ____      _    __  __ "
   print "|  _ \| \ | |  / \     / ___|  _ \ \ / /  _ \_   _/ _ \ / ___|  _ \    / \  |  \/  |"
   print "| | | |  \| | / _ \   | |   | |_) \ V /| |_) || || | | | |  _| |_) |  / _ \ | |\/| |"
   print "| |_| | |\  |/ ___ \  | |___|  _ < | | |  __/ | || |_| | |_| |  _ <  / ___ \| |  | |"
   print "|____/|_| \_/_/   \_\  \____|_| \_\|_| |_|    |_| \___/ \____|_| \_\/_/   \_\_|  |_|"
   print "                                                                                    "
   print "               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                "
   print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display any found system files to the user.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

   print "Plain Text File [",
   if os.path.exists('./plain.txt'):
      print colored("plain.txt",'green'),
      print "]"
   else:
      print "]"
   print "Encrypted File  [",
   if os.path.exists('./encrypted.enc'):
      print colored("encrypted.enc",'red'),
      print "]\n"
   else:
      print "]\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create a main controller.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

   options=menu.keys()
   options.sort()
   for entry in options: 
      print entry, menu[entry]
   selection=raw_input("\nPlease Select: ")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Create a plain text message & store it in plain.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='1':
      if os.path.exists('./plain.txt'):
         print "Plain.txt file already exists...\n"
         exit(1)
      message = raw_input("\nType your secret message here: ")
      os.system("echo " + message + " > plain.txt")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Encrypt message (text.txt) & output it to text.enc
# Modified: N/A
# -------------------------------------------------------------------------------------

# Step 1: Convert all ASCII values to an 8-bit binary value.
# Step 2: Convert each binary value to a A,C,T,G quartet combination based on mappings like this {"A":"00", "C":"01", "G":"10", "T":"11"}
# Step 3: Convert each A,C,T,G quartet combination to an extended ASCII character based on the substitution table.

   if selection =='2':
      if os.path.exists('./encrypted.enc'):
         print "Encrypted.enc file already exists...\n"
         exit(1)
      else:
         if os.path.exists('./plain.txt'):
            bits2base = {"00":"A", "01":"C", "10":"G", "11":"T"}
         else:
            print "Plain.txt file not found....\n"
            exit(1)

      # Construct a random table that represent all the 256 different possible quartet combinations of A,C,T,G
      table = [''.join(x) for x in itertools.product('ATCG', repeat=4)]
      random.shuffle(table)
      assert(len(table)==256)

      # Write the table to a file named key.txt
      with open('key.txt', 'wt') as f:
          for x in table:
              f.write(x)

      # Open the plain text file for encryption and write to encrypted.enc
      with open('plain.txt', 'rt') as inf, open('encrypted.enc', 'wb') as outf:
          text = inf.read()
          for ch in text:
              binary = '{0:08b}'.format(ord(ch))
              bit_pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
              base_quartet = ""
              for x in bit_pairs:
                  base_quartet += bits2base[x]
              outf.write(chr(table.index(base_quartet)))

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Delete the secret message (plain.txt)
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='3':
      if os.path.exists('plain.txt'):
         os.system("rm plain.txt")
      else:
         print "Plain.txt file not found..."
         exit(1)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Decrypt text.enc & output it to text.txt (message)
# Modified: N/A
# -------------------------------------------------------------------------------------

# Step 1: Convert each extended ASCII character to an A,C,T,G quartet combination based on the substitution table.
# Step 2: Convert each A,C,T,G quartet combination to its binary value using a mapping like this {"A":"00", "C":"01", "G":"10", "T":"11"}
# Step 3: Convert each 8-bit binary value to its ASCII value (this forms the decrypted message).

   if selection =='4':
      if os.path.exists('./encrypted.enc'):
         base2bits = {"A":"00", "C":"01", "G":"10", "T":"11"}
      else:
         print "Encrypted.enc file not found...\n"
         exit(1)
      if os.path.exists('./plain.txt'):
         print "Plain.txt file already exists...\n"
         exit(1)

      # Read the substitution table from a file named key.txt
      table = []
      with open('key.txt', 'rt') as f:
         seq = f.read()
         for quartet in [seq[i:i+4] for i in range(0, len(seq), 4)]:
            table.append(quartet)
      
      assert(len(table)==256)

      # Open encrypted.enc for decryption and write to plain.txt
      with open('encrypted.enc', 'rb') as inf, open('plain.txt', 'wt') as outf:
         data = inf.read()
         for byte in data:
            base_quartet = table[ord(byte)]
            binary = ""
            for base in  base_quartet:
               binary += base2bits[base]
            outf.write(chr(int(binary, 2)))

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Read secret message.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='5':
      if os.path.exists('plain.txt'):
         print ""
         os.system("cat plain.txt")
         raw_input("\nPress any key to continue...")         
      else:
         print "Plain.txt file not found..."
         exit(1)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Exit the program.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='6':
      if os.path.exists('encrypted.enc'):
         os.remove('encrypted.enc')
      if os.path.exists('plain.txt'):
         os.remove('plain.txt')
      exit(1)

