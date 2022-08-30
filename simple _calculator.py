a=int(input("enter the first number="))
b=int(input("enter the second number="))
print("1.addition")
print("2.substract")
print("3.multiplication")
print("4.division")
ch=int(input("enter your choice="))
if(ch==1):
    result=a+b
    print(result)
elif(ch==2):
    result=a-b
    print(result)
elif(ch==3):
    result=a*b
    print(result)
elif(ch==4):
    result=a/b
    print(result)
else:
    print("wrong choice")

