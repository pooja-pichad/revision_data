a=[2,4,6,8]
i=1
k=a[0]
b=[]
# k=a[0]
while i<len(a):
    t=a[i]
    c=t-k
    b.append(c)
    k=t
    i=i+1
print(b)

# i=1
# b=[]
# while i<len(a):
#     t=a[0]
#     c=t**1
#     b.append(c)
#     i=i+1
# print(b)
