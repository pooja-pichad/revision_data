a=["1","2","3"]

i=0
k=[]
while i<len(a):
    t=a[i]
    p=t+a[i+1]
    k.append(p)
    i=i+2
    break
print(k)