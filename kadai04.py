import re
import pprint
import numpy as np

f=open("FEH_00200521_220610143730.csv",encoding="UTF-8")
data=f.readlines()

num1 = "0"
i=1
list = []
for t in range(9)  :
    for datax in data:
        n=str(i)
        num1 = "0"+n+"000"
        if datax.startswith(num1):
            list1=[]
            for line in datax.split('","'):
                line1 = line.strip()
                if line1:
                    list1.append(line1)
                else:
                    if list1:
                        #print(",".join(list1))
                        list1.char()
            list.append(list1)
            #print(datax)
    i=i+1
l=10
for t in range(9,47)  :
    for datax in data:
        n=str(l)
        num1 = n+"000"
        if datax.startswith(num1):
            list2=[]
            for line in datax.split('","'):
                line1 = line.strip()
                if line1:
                    list1.append(line1)
                else:
                    if list1:
                        #print(",".join(list1))
                        list1.char()
            list.append(list2)
            #print(datax)
    l=l+1
#listde=list(filter(None,list))
np.array(list)
#np.delete(list,0,0)
#x = np.mean(list,axis=2)
#print(x)
#print("平均値："+np.mean(nplist,axis=2))
#print("中央値："+np.median(nplist,axis=2))
#print("最小値："+np.min(nplist,axis=2))
#print("分散："+np.var(nplist,axis=2))
#print("標準偏差："+np.std(nplist,axis=2))

print("last")
print(list)
#pprint.pprint(list,width=50)
f.close()
print("fin")
