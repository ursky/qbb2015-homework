#! /usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt



file=pd.read_table ("output.txt")





plt.figure()
plt.hist(file["S"], bins=100, log=False, range = (0,200))
plt.savefig("Scores_histogram.png")


plt.figure()
plt.hist(file["E"], bins=100, log=False)
plt.savefig("E_val_histogram.png")


