num=int(input("enter a number"))
a=[1,2,4,5,7,9,2]
i=0
k=[]
while i<len(a)-num:
    k.append(a[i])
    i=i+1
j=1
while j<=num:
    k.append(a[-j])
    j+=1
print(k)
