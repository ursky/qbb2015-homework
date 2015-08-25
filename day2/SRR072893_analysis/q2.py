#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/genomes/BDGP6.sam"

file = open(filename)

count=0

for data in file:
        
    if "NM:i:0" in data:
        count+=1

print count
    
    
    
file.close()