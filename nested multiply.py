a=[1,2,[4,5],7,9,2,6]
i=0
product=1
while i<len(a):
    n=a[i]
    if type(n)==list:   
        for j in range(len(n)):
            product=product*n[j]
    else:
        product=product*n

    i=i+1
print(product)



# a=[1,2,[4,5],6,7,8]
# i=0
# p=1
# while i<len(a):
#     if type(a[i])==list:
#         for j in range(len(a[i])):
#             p=p*a[i][j]
#     else:
#         p=p*a[i]
#     i=i+1
# print(p)





