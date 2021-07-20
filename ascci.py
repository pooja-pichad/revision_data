num=int(input("enter a number"))
k=65
i=0
while i<num:
    j=0
    while j<i+1:
        a=chr(k)
        print(a,end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1