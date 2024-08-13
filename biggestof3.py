a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
if (a>b) and (a>c):
    print("{} is greater".format(a))
elif (b>c) and(b>a):
    print("{} is greater".format(b))
else:
    print("{} is greater".format(c))
