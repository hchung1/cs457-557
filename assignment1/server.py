#!/usr/bin/env python

"""Simple server application"""

from serverpart_substitution import conversion
from similarities import *

import socket
import pickle as pk

alphebet="abcdefghijklmnopqrstuvwxyz"
cap_alph = alphebet.upper()
#intergers="0123456789 "
#special_char="\",./?><\'\\{}[]=-_+()*&^%$#@!~`|"
strings=alphebet+cap_alph # +intergers+special_char

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) 
s.listen(backlog)
while 1:
    print ('Server ready, willing and able!')
    client, address = s.accept()
    data = pk.loads(client.recv(size))
    print data[0]
    if data[0] == 'Begin':
        client.send('Y')
        while data[0] != "End":
            data = pk.loads(client.recv(size))
            if data[0] == "Translate":
                result=conversion(data[1],strings)
                client.send(result)
            if data[0] == "End":
                client.send("...")
                client.close()
