# fibonacci series
n=int(input("enter the limit="))
first=0
second=1
third=0
print(first,second,end=" ")
for i in range(n):
    third=first+second
    first=second
    second=third
    print(third,end=" ")
