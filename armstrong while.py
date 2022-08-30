# check the number is armstrong or not
n=int(input("enter the number="))
sum=0
count=0
num=num1=n
while(n>0):
    d=n%10
    count=count+1
    n=n//10
# print(count)
while(num>0):
    d=num%10
    sum=sum+d**count
    num=num//10
if(num1==sum):
    print(sum,"is armstrong")
else:
    print(sum,"not an armstrong")