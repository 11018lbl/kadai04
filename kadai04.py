import pprint


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
            list.append(datax)
            print(datax)
    i=i+1
l=10
for t in range(9,47)  :
    for datax in data:
        n=str(l)
        num1 = n+"000"
        if datax.startswith(num1):
            list.append(datax)
            print(datax)
    l=l+1

print("last")
pprint.pprint(list,width=50)
f.close()
print("fin")
