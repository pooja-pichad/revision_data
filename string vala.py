a=["1","2","3","4","5","6","7","8"]

i=0
k=[]
while i<len(a):
    t=a[i]
    k.append(t+a[i+1])
    i=i+2
print(k)