#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/genomes/BDGP6.sam"

file = open(filename)

count=0

for data in file:
    line=data.split()
    
    if line[0]!="@SQ" and line[0]!="@HD":
        count+=1

    
    
print count
    
file.close()