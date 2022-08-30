#nested if  is if in a if
# chech the number is positive
n=int(input("enter the number="))
if(n>0):
    print("number is positive")
else:
    if(n<0):
        print("number is negative")
    else:
        print("zero")
