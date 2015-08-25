#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/genomes/BDGP6.sam"

file = open(filename)


for data in file:
    print data,
    
file.close()