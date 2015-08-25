#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/genomes/BDGP6.sam"

file = open(filename)

count=0

for data in file:
    line=data.split()
    
    if "@" not in line[0]:
        count+=1
        print line[2]
    
    if count==10:
        break
    
    
file.close()