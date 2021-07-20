

# name= input("enter a name ")
# i=0
# while i<len(name):
#     print(name.upper()[i]+i*(name[i]),end="")
#     if i!=len(name)-1:
#         print("_",end="")
#     i=i+1

# name= input("enter a name ")
# i=0
# while i<len(name):
#     if i==0:
#         print(name.upper()[i],end="")
#     else:
#         print(name[i]+i*(name[i]),end="")
#     if i!=len(name)-1:
#         print("_",end="")
#     i=i+1

# a=["1","2","3"]
# i=0
# c=[]
# while i<len(a[i]):
#     b=a[i]
#     t=b+a[i+1]
#     c.append(t)
#     i+=1
#     print(c)
    

a=[{"maths":40,"eng":10},{"maths":20,"eng":30}]
b=input("enter subject:")
i=0
while i<len(a):
    c=a[i]
    if b in c:
        print(a[i][b])
    i+=1