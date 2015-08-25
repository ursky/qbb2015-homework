#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/genomes/BDGP6.sam"

file = open(filename)

n2L=0 
n2R=0 
n3L=0
n3R=0 
n4=0
nX=0

count=0

for data in file:
    line=data.split()
    
    if "@" not in line[0]:
        if count>100:
            pass
                    
        if line[2]=="2L":
            n2L+=1
        if line[2]=="2R":
            n2R+=1
        if line[2]=="3L":
            n3L+=1
        if line[2]=="3R":
            n3R+=1
        if line[2]=="4":
            n4+=1
        if line[2]=="X":
            nX+=1
            
        count+=1
    
print "2L = ", n2L
print "2R = ", n2R
print "3L = ", n3L
print "3R = ", n3R
print "4 = ", n4
print "X = ", nX
    
    
file.close()