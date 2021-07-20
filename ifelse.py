 num=int(input("enter a number"))
i=1
while i<=num:
    if i%3==0 and i%7==0:
        print("bye")
    elif i%3==0:
        print("hi")
    elif i%7==0:
        print("hello")
    else:
        print(i)
    i=i+1