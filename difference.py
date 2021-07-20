a=[1,2,3,4,5,6,7,8,9,10]


i=1
b=[]
while i<len(a):
    t=a[i]
    b.append(t-i)
    i=i+1
print(b)