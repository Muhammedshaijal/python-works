#sum of digit of n numbers
# n=int(input("enter the number="))      
# sum=0
# while(n>0):            #
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum,"is the sum")

#sum of digits squres of a number
# n=int(input("enter the number="))
# sum=0
# while(n>0):
#     d=n%10
#     d*=d
#     sum=sum+d
#     n=n//10
# print(sum)

# check the number is armstrong or not
n=int(input("enter the number="))
sum=0
num=n
count=0
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10
if(num==sum):
    print(sum,"is armstrong")
else:
    print(sum,"not an armstrong")


