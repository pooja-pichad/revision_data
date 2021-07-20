# a=[5,6,7,8,2,9,3,1]
# l=len(a)
# for i in range(0,l):
#     c=0
#     for j in range(2,a[i]):
#         if a[i]%j==0:
#             c=1
#             break
#     if c==0:
#         print(a[i],"prime number")
#     else:
#         print(a[i],"not prime number")


a=[5,6,7
,[8],2,[9,3],1]
# l=len(a)
# for i in range(0,l):
#     c=0
#     for j in range(2,a[i][j]):
#         if a[i]%j==0  or a[j]%j==0:
#             c=1
#             break
#     if c==0:
#         print(a[i],a[j],"prime number")
#     else:
#         print(a[i],a[j],"not prime number")
i=0
while i<len(a):

    if i==2 or i==3 or i==5 or i==7:
        print("prime number",i)
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
        print("not prime number",i)
    else:
        print("prime number",i)
    i=i+1