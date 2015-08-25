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
total=0

for data in file:
    line=data.split()
    
    if "@" not in line[0]:
        if count>100:
            pass
        
        total+=int(line[4])
        count+=1
    
print total/count

    
file.close()