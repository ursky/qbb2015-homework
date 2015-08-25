#! /usr/bin/env python

import pandas

annotation_file="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
f=open(annotation_file)

data=pandas.read_table(f, comment='#', header=None)

#print data
#print data.head()

#print data.describe()
#print data.info()

#print data[1:5]

data.columns=["chromosome","database","type","start","end","score","strand","frame","attributes"]

#print data.sort(columns="start", ascending=True)
#print data.sort(columns="start", ascending=True)


#print data["chromosome"]
#print data[["chromosome","start", "end"]]
#print data["start"][9:15]

#print data.shape
#data2=data["start"]
#print data2.shape
#print data2

#saving new file
#data2=data["start"]
#data2.to_csv("startColumn.txt", sep='\t', index=False)

region_of_interest = data["start"]<10
#print region_of_interest
print data[region_of_interest]
print data[region_of_interest].shape
