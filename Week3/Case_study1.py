# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:33:29 2020

@author: Andre
"""
import string 

alphabet = " " + string.ascii_lowercase
    
    tab = {
        " ": 0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5,
        'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11,
        'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17,
        'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23,
        'x':24, 'y':25, 'z':26 }

 tab = {
        " ": '0', 'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5',
        'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11',
        'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17',
        'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23',
        'x':'24', 'y':'25', 'z':'26' }

message = "hi my name is caesar"   
    
encoded_message = ""
for i in range(0, len(message)):
        word = message[i]
        count = tab[word]
        count2 = count + 1
        
        encoded_message += str(count)



