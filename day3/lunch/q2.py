#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt



data=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM_raw=data["FPKM"]
FPKM=[]
for i in FPKM_raw:
    if i!=0:
        FPKM.append(i) 
 
 
plt.figure()
plt.hist(FPKM, bins=100, log=False)
#plt.savefig("FPKM_hist.png")

plt.show()
 
