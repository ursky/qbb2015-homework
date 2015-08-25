#! /usr/bin/env python


filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

file = open(filename)

#print the whole file line by line

for line_count, data in enumerate(file):
    #f=data.split()
    
    if line_count in range (10,15):
        print data,
    if line_count>15:
        break
        
file.close()