#! /usr/bin/env python

import pandas
import matplotlib.pyplot as plt

annotation_file="/Users/cmdb/qbb2015/rawdata/samples.csv"
f=open(annotation_file)

data=pandas.read_table(f, sep=",")
names=data["sample"]

for i in names:
    filename = "/Users/cmdb/qbb2015/stringtie/%s/t_data.ctab" % (str(i))
    file=open(filename)
    data=pandas.read_table(file)
    
    roi=data["t_name"].str.contains("FBtr0331261")
    out = data[roi]
    
    print out