n=int(input("enter the value:"))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c


