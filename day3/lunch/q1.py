#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt



metadata=pd.read_csv("~/qbb2015/rawdata/samples.csv")




#females
sxl_f=[]
for sample in metadata[metadata["sex"]=="female"]["sample"]:
    data_f=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    
    roi=data_f["t_name"].str.contains("FBtr0331261")
    sxl_f.append(data_f[roi]["FPKM"].values)

#males
sxl_m=[]
for sample in metadata[metadata["sex"]=="male"]["sample"]:
    data_m=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    
    roi=data_m["t_name"].str.contains("FBtr0331261")
    sxl_m.append(data_m[roi]["FPKM"].values)



metadata2=pd.read_csv("~/qbb2015/rawdata/replicates.csv")


#females
sxl_fr=[0,0,0,0]
for sample in metadata2[metadata2["sex"]=="female"]["sample"]:
    data_fr=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    
    roi=data_fr["t_name"].str.contains("FBtr0331261")
    sxl_fr.append(data_fr[roi]["FPKM"].values)
    


xlabels=[]
xticks=[]
count=0
for stage in metadata["stage"]:
    if count>7:
        break
    xlabels.append(stage)
    xticks.append(count)
    count+=1


plt.figure()
plt.plot(sxl_f, 'r', label='Female')
plt.plot(sxl_m, 'b', label='Male')
plt.plot(xticks, sxl_fr, 'o')
#plt.plot(sxl_fr, 'r', label='Replicates')

plt.xticks(xticks, xlabels, rotation='vertical')
plt.title('Sxl', fontsize='x-large')
plt.legend(loc='upper left', fontsize='x-large')
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")

plt.savefig("timecourse.png")



################# replicaties



