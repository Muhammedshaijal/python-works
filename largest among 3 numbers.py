a=int(input("enter the fist number="))
b=int(input("enter the second number="))
c=int(input("enter the third number="))
if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(c,"is greater")
elif(c>a and c>b):
    print(c,"is greater")
else:
    print("all equal")
