#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

file = open(filename)

#print the whole file line by line
for data in file:
    f=data.split()
    if "tRNA" in f[9]:
        print f
        
file.close()