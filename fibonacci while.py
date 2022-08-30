# fibonacci  0,1,1,2,3,5,8,13
n=int(input("enter the limit="))
first=0
second=1
third=0
print(first,second,end=" ")
for i in range(2,8):
    third=first+second
    first=second
    second=third
    print(third,end=" ")
