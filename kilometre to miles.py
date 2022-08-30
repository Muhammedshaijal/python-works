print("1.kilometre into miles")
print("2.miles into kilometre")
n=int(input("enter your choice="))
if n==1:
    km=float(input("enter the kilometre="))
    m=km*0.62137
    print("mile is=",round(m,2))
elif n==2:
    m=float(input("enter the miles="))
    km=m/1.6
    print("kilometre is=",round(km,2))
else:
    print("invalid choice")
