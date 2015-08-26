#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde



data=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKM_raw=data["FPKM"]
FPKM=[]
for i in FPKM_raw:
    if i!=0:
        FPKM.append(i)

density = gaussian_kde(FPKM)


xs = np.arange(0,2000,1)
ys = density(xs)


plt.figure()
plt.plot(xs,ys)
plt.show()
plt.savefig("FPKM_distribution.png")
 


