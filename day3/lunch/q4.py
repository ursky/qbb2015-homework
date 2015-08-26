#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde



data1=pd.read_table("~/qbb2015/stringtie/SRR072897/t_data.ctab")
data2=pd.read_table("~/qbb2015/stringtie/SRR072898/t_data.ctab")

#      [   data1   :   data2   :   M(difference)   :   A(average)   ]
data=[[],[],[],[]]

for i in data1["FPKM"]:
    data[0].append(i)
    
for i in data2["FPKM"]:
    data[1].append(i)

for i in range (0, len(data[1])):
    data[2].append(np.log2(data[0][i])-np.log2(data[1][i]))
    data[3].append((np.log2(data[0][i])+np.log2(data[1][i]))/2)
    

plt.figure()
plt.plot(data[3], data[2], 'o')
plt.xlabel("A value")
plt.ylabel("M value")
plt.title("MA plot of SRR072897 vs SRR072898")
plt.savefig("MA_graph.png")
#plt.show()