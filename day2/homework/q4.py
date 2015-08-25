#! /usr/bin/env python

import pandas
import matplotlib.pyplot as plt









annotation_file="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
f=open(annotation_file)

data=pandas.read_table(f)
FPKM_values=data["FPKM"]


top=FPKM_values[0:11572]
mid=FPKM_values[11572:23145]
bot=FPKM_values[23145:34717]

plt.figure()
plt.boxplot([top, mid, bot])
#plt.boxplot(mid)
#plt.boxplot(bot)


#plt.xlabel("Sequence identifier")
#plt.ylabel("Start position on genome")

plt.savefig("q4_output.png")
