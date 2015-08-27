#! /usr/bin/env python

''''
count intersection between Bed files
'''

import numpy as np
import sys
import copy
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt
import numpy as np


def arrays_from_len_file(file):
    arrays={}
    for line in open(file):
        fields=line.split()
        name=fields[0]
        size=int(fields[1])
        arrays[name]=np.zeros(size, dtype=bool)
    
    return arrays
    
    
def mark_arrays (filename, arrays):
    for line in open(filename):
        fields=line.split()
        chromosome=fields[0]
        start=int(fields[1])
        end=int(fields[2])
        
        arrays[chromosome][start:end]=1
        
    return arrays


#_________________________________________


    

A_name="DM3_Kc_BEAF.bed"
B_name="DM3_Kc_CTCF.bed"
C_name="DM3_Kc_SuHW.bed"

blank=arrays_from_len_file( "dm3.len" )
A_array=mark_arrays(A_name, blank)

blank=arrays_from_len_file( "dm3.len" )
B_array=mark_arrays(B_name, blank)

blank=arrays_from_len_file( "dm3.len" )
C_array=mark_arrays(C_name, blank)

#_________________________________________





A=0
B=0
C=0
AB=0
AC=0
BC=0
ABC=0


for line in open(A_name):
    fields=line.split()
    chromosome=fields[0]
    start=int(fields[1])
    end=int(fields[2])
    
    slB=B_array[chromosome][start:end]
    slC=C_array[chromosome][start:end]

    if slB.any()==False and slC.any()==False:
        A+=1
    
    if slB.any()==True and slC.any()==True:
        ABC+=1
    
    if slB.any()==True and slC.any()==False:
        AB+=1
        
    if slB.any()==False and slC.any()==True:
        AC+=1



#_________________________________________



for line in open(B_name):
    fields=line.split()
    chromosome=fields[0]
    start=int(fields[1])
    end=int(fields[2])
    
    slA=A_array[chromosome][start:end]
    slC=C_array[chromosome][start:end]

    if slA.any()==False and slC.any()==False:
        B+=1
    
    if slA.any()==True and slC.any()==True:
        ABC+=1
    
    if slA.any()==True and slC.any()==False:
        AB+=1
        
    if slA.any()==False and slC.any()==True:
        BC+=1


#_________________________________________




for line in open(C_name):
    fields=line.split()
    chromosome=fields[0]
    start=int(fields[1])
    end=int(fields[2])
    
    slB=B_array[chromosome][start:end]
    slA=A_array[chromosome][start:end]

    if slA.any()==False and slB.any()==False:
        C+=1
    
    if slA.any()==True and slB.any()==True:
        ABC+=1
    
    if slA.any()==True and slB.any()==False:
        AC+=1
        
    if slA.any()==False and slB.any()==True:
        BC+=1
    
    
AB=AB/2
AC=AC/2
BC=BC/2
ABC=ABC/3

print "A ", A
print "B ", B
print "C ", C
print "AB ", AB
print "AC ", AC
print "BC ", BC
print "ABC ", ABC
print "\n"

#_________________________________________



plt.figure()
v = venn3(subsets=(A, B, AB, C, AC, BC, ABC), set_labels = ('BEAF', 'CTCF', 'SuHW'))
#plt.show()
plt.savefig("VENN_diagram.png")
















