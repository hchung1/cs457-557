#!/usr/bin/env python

"""Simple client application"""

from similarities import *

import socket
import pickle as pk

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

data=""
command = ""
print ("do you want to connect to the server?")
answer = str(raw_input("\ny/n? >>\n"))
if answer == 'y':
    answer = ('Begin', '')
    s.send(pk.dumps(answer))
    data = s.recv(size)
    print data
if data == 'Y':
    while data != "...":
        print ("translate or 'end'")
        string=str(raw_input("Command?\n>> "))
        if string == "translate":
            string = str(raw_input("What do you want to translate?>>"))
            answer = ("Translate", string)
            s.send(pk.dumps(answer))
            data = s.recv(size)
            print data
        if string == "end":
            answer = ("End",'')
            s.send(pk.dumps(answer))
            data = s.recv(size)
            s.close()
