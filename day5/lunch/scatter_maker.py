#! /usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file=pd.read_table ("output.txt")





plt.figure()
plt.plot(-np.log10(file["E"]), np.log10(file["S"]), 'o')
plt.xlabel("log of e-value")
plt.ylabel("log of Score")

plt.savefig("Scores_vs_eValues_scatter.png")
