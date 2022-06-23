import re
import pprint
import numpy as np
import csv
import pandas as pd

#f=open("FEH_00200521_220610143730.csv",encoding="UTF-8")
#data=f.readlines()
with open("FEH_00200521_220610143730.csv",'r',encoding="UTF-8") as f:
    reader=csv.reader(f)
    n=0
    list = []

    for row in reader:
        if n >1:
            code=row[0]
            area=row[1]
            number=re.sub("(,)",'',row[2])
            if code[2:5] == '000':
                #print(code,area,number)
                list.append(int(number))

        n += 1

print("平均値："+str(np.mean(list)))
print("中央値："+str(np.median(list)))
print("最小値："+str(np.min(list)))
print("分散："+str(np.var(list)))
print("標準偏差："+str(np.std(list)))

f.close()

"""
num1 = "0"
list = []
p1='[0-9],[a-xA-Z0-9_]|[a-xA-Z0-9],[0-9]|","'

for i in range(1,10)  :
    for datax in data:
        n=str(i)
        num1 = "0"+n+"000"
        if datax.startswith(num1):
            list1=[]
            for line in datax.split(p1):
                line1 = line.strip()
                if line1:
                    list1.append(line1)
                else:
                    if list1:
                        #print(",".join(list1))
                        list1.char()
            list.append(list1)
#            list.append(datax)
            #print(datax)
    #i=i+1

for l in range(9,47)  :
    for datax in data:
        n=str(l)
        num1 = n+"000"
        if datax.startswith(num1):
            list2=[]
            for line in datax.split(p1):
                line2 = line.strip()
                if line2:
                    list1.append(line2)
                else:
                    if list1:
                        #print(",".join(list1))
                        list1.char()
            list.append(list2)
#            list.append(datax)
            #print(datax)
    #l=l+1

liststr=[[]for i in range(46)]

for counter1 in range(46):
    listdash=str(list[counter1])
    cut = listdash.split(p1)
    print(cut)

#listde=list(filter(None,list))
#np.array(list)
#np.delete(list,0,0)
#x = np.mean(list,axis=)
#print(x)
#print("平均値："+np.mean(nplist,axis=2))
#print("中央値："+np.median(nplist,axis=2))
#print("最小値："+np.min(nplist,axis=2))
#print("分散："+np.var(nplist,axis=2))
#print("標準偏差："+np.std(nplist,axis=2))

print("last")
print(list)
print(list[1][0])
#pprint.pprint(list,width=50)
f.close()
print("fin")
"""
