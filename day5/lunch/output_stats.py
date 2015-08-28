#! /usr/bin/env python

import sys


file=open("outout.txt")


while 1:
    line = file.readline()
    
    if line.startswith("~"):
        break
        
    if line.startswith(">") or line.startswith(" Identities"):
        print line.lstrip("> ").rstrip("\n")
    

