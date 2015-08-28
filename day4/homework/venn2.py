#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt
import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname="dm3.len" )

B_name="DM3_Kc_BEAF.bed"
C_name="DM3_Kc_CTCF.bed"
S_name="DM3_Kc_SuHW.bed"

B_arr = arr.copy()
C_arr = arr.copy()
S_arr = arr.copy()

B_arr.set_bits_from_file(fname=B_name)
C_arr.set_bits_from_file(fname=C_name)
S_arr.set_bits_from_file(fname=S_name)

B_arr.Chrom_Start_End(fname=B_name)
C_arr.Chrom_Start_End(fname=C_name)
S_arr.Chrom_Start_End(fname=S_name)

comp_table = arr.compare(B_arr, C_arr, S_arr)
print comp_table


plt.figure()
v = venn3(subsets=comp_table, set_labels = ('BEAF', 'CTCF', 'SuHW'))
#plt.show()

plt.savefig("VENN_with_class")

