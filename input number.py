n=int(input("enter the number="))
if n%5==0 and n%7==0:
    print("divisible by both 5 and 7")
elif n%5==0:
    print("it is divisible by 5")
elif n%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by both 5 and 7")