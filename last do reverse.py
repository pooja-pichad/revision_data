# num=int(input("enter a number"))
# a=(num//1)%10
# if num>=0:
#     print(a)


a=int(input("enter number"))
if a%3==0 and a%5==0:
    print("by")
elif a%3==0:
    print("hi")
elif a%5==0:
    print("hello")
else:
    print(a)