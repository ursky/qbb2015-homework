#! /usr/bin/env python


import sys
import pandas
import matplotlib.pyplot as plt


#new way to input file - just pass /Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf as an argument when running in terminal
#print sys.argv
#annotation_file=sys.argv[1]
#f=open(annotation_file)

#OR:
f=sys.stdin
#run by printing :
#cat /Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf | ./demo.py
#or:
#./demo.py < /Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf

data=pandas.read_table(f, comment='#', header=None)
data.columns=["chromosome","database","type","start","end","score","strand","frame","attributes"]


print "\n\n\n\n",data.shape,"\n\n\n\n\n"

