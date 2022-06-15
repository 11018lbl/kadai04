print("hello world")
f=open("test.txt")
txt=f.readlines()
print(txt[1])
print(txt[0])
print(txt[2])
f.close()

f=open("FEH_00200521_220610143730.csv",encoding="UTF-8")
data=f.readlines()

num1 = "0"
num2 ="0"
i=1
for t in range(9)  :
    for datax in data:
        n=str(i)
        num1 = "0"+n+"000"
        if datax.startswith(num1):
            print(datax)
    i=i+1
l=10
for t in range(9,47)  :
    for datax in data:
        n=str(l)
        num1 = n+"000"
        if datax.startswith(num1):
            print(datax)
    l=l+1

print("last")
f.close()
print("fin")
