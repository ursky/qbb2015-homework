#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


data=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
print data


roi=data[data.FPKM !=0]

start=roi["start"]
FPKM=roi["FPKM"]

    
plt.figure()
plt.scatter(start,FPKM)
plt.savefig("FPKM_scatter.png")

 


