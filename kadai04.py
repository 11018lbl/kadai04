import re
import numpy as np
import csv

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
