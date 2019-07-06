#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#           PYTHON UTILITY FILE TO ENCODE AND DECODE DNA-BASED CRYPTOGRAMS
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load any required imports and initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import os.path
import random
import itertools
from termcolor import colored	# pip install termcolor

message = ""
dnacode = ""
cryptoG = ""

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create a main menu system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

menu = {}
menu['(1)']="Create message."
menu['(2)']="Encrypt message."
menu['(3)']="Delete message."
menu['(4)']="Decrypt message."
menu['(5)']="Clean files and exit."

while True: 
   os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------
   print " ____  _   _    _       ____ ______   ______ _____ ___   ____ ____      _    __  __ "
   print "|  _ \| \ | |  / \     / ___|  _ \ \ / /  _ \_   _/ _ \ / ___|  _ \    / \  |  \/  |"
   print "| | | |  \| | / _ \   | |   | |_) \ V /| |_) || || | | | |  _| |_) |  / _ \ | |\/| |"
   print "| |_| | |\  |/ ___ \  | |___|  _ < | | |  __/ | || |_| | |_| |  _ <  / ___ \| |  | |"
   print "|____/|_| \_/_/   \_\  \____|_| \_\|_| |_|    |_| \___/ \____|_| \_\/_/   \_\_|  |_|"
   print "                                                                                    "
   print "              BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                 "
   print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display found system files and variable data to the user.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

   print "Message   :",
   print colored(message,'blue') 
   
   print "DNA Code  :", 
   if os.path.exists('plain.txt'):
      print colored(dnacode,'white')
   else:
      print ""
   print "Crytogram :",
   if os.path.exists('encrypted.enc'):
      cryptoG = open("encrypted.enc").readline().rstrip()
      print colored(cryptoG,'yellow')
   else:
      print "" 
   print "\nPlain Text File [",
   if os.path.exists('plain.txt'):
      print colored("plain.txt",'blue'),
      print "]"
   else:
      print "]"
   print "Encrypted File  [",
   if os.path.exists('./encrypted.enc'):
      print colored("encrypted.enc",'yellow'),
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
         raw_input("\nSorry, plain text file already exists...?")
      else:
         message = raw_input("\nType your plain text message here: ")
         os.system("echo " + message + " > plain.txt")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Encrypt message (text.txt) & output it to text.enc
# Modified: N/A
# Method  : 1. Convert 8-bit binary values to ASCII values
#         : 2. Convert quartet combinations to binary by mapping A:00 C:01 G:10 T:11
#         : 3. Convert ASCII to A,C,T,G quartet-combinations via the substitution table
# -------------------------------------------------------------------------------------

   if selection =='2':
      if os.path.exists('./encrypted.enc'):
	 raw_input("\nSorry, encrypted.enc file already exists...?")
      else:
         if os.path.exists('./plain.txt'):
            bits2base = {"00":"A", "01":"C", "10":"G", "11":"T"}
            table = [''.join(x) for x in itertools.product('ATCG', repeat=4)]
            random.shuffle(table)
            assert(len(table)==256)           
            with open('key.txt', 'wt') as f:
               for x in table:
                  f.write(x)           
            with open('plain.txt', 'rt') as inf, open('encrypted.enc', 'wb') as outf:
               text = inf.read()
               for ch in text:
                 binary = '{0:08b}'.format(ord(ch))
                 bit_pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
                 base_quartet = ""
                 for x in bit_pairs:
                     base_quartet += bits2base[x]
                     dnacode = dnacode + base_quartet
                 outf.write(chr(table.index(base_quartet)))
         else:
            raw_input("\nSorry, plain.txt file was not found...?")

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
         message = ""
      else:
         raw_input("\nSorry, plain.txt file was not found...?")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Decrypt text.enc & output it to text.txt (message)
# Modified: N/A
# Method  : 1. Convert ASCII to A,C,T,G quartet-combinations via the substitution table
#         : 2. Convert quartet combinations to binary by mapping A:00 C:01 G:10 T:11
#         : 3. Convert 8-bit binary values to ASCII values - forms decrypted message
# -------------------------------------------------------------------------------------

   if selection =='4':
      if os.path.exists('./encrypted.enc'):
         base2bits = {"A":"00", "C":"01", "G":"10", "T":"11"}
         table = []
         with open('key.txt', 'rt') as f:
            seq = f.read()
            for quartet in [seq[i:i+4] for i in range(0, len(seq), 4)]:
               table.append(quartet)
         assert(len(table)==256)
         with open('encrypted.enc', 'rb') as inf, open('plain.txt', 'wt') as outf:
            data = inf.read()
            for byte in data:
               base_quartet = table[ord(byte)]
               binary = ""
               for base in base_quartet:
                  binary += base2bits[base]
               outf.write(chr(int(binary, 2)))
         message = open("plain.txt").readline().rstrip()
      else:
         raw_input("\nSorry, encrypted.enc file was not found...?")      

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Exit the program.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='5':
      if os.path.exists('encrypted.enc'):
         os.remove('encrypted.enc')
      if os.path.exists('plain.txt'):
         os.remove('plain.txt')
      if os.path.exists('key.txt'):
         os.remove('key.txt')
      exit(0)

#End
