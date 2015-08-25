#! /usr/bin/env python

import pandas
import matplotlib.pyplot as plt

annotation_file="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
f=open(annotation_file)
data=pandas.read_table(f, comment='#', header=None)
data.columns=["chromosome","database","type","start","end","score","strand","frame","attributes"]


roi=data["attributes"].str.contains("Sxl")

plt.figure()
plt.plot(data[roi]["start"])
plt.xlabel("Sequence identifier")
plt.ylabel("Start position on genome")
plt.savefig("q1_output.png")


