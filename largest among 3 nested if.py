# largest among 3 numbers
a=int(input("enter the 1st number="))
b=int(input("enter the 2nd number="))
c=int(input("enter the 3rd number="))
if(a>b):
    if(a>c):
        print(a,"is large")
    else:
        print(c,"is large")
else:
    if(b>c):
        print(b,"is large")
    else:
        print(c,"is large")