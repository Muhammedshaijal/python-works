n=int(input("enter the number="))
count=0
for i in range(1,n+1,1):
    if(n%i==0):
        count=count+1
# print(count)
if count==2:
    print("is prime")
else:
    print("not prime")
