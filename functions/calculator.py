def sum(a,b):
    c=a+b
    print("sum is ",c)
def sub(a,b):
    c=a-b
    print('sub is',c)
def mul(a,b):
    c=a*b
    print("mul is ",c)
def div(a,b):
    c=a/b
    print("div is",c)
while(1):
    print("1.addition")
    print("2.substract")
    print("3.multiplication")
    print("4.division")
    a = int(input("enter the first number="))
    b = int(input("enter the second number="))
    ch=int(input("enter your choice="))

    if ch==1:
      sum(a,b)
    elif ch==2:
      sub(a,b)
    elif ch==3:
      mul(a,b)
    elif ch==4:
      div(a,b)
    else:
        print("wrong choice")
        break