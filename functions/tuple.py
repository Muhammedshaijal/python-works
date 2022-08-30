# tuple      is immutale it does not change
# tuple(2,6,'shij',5) #enclosed in a simple brace
# tuple1=(1,2,3,4,'anu',1,1)
# print(tuple1)
# print(len(tuple1))
# print(tuple1.count(1)) #use to count
# print(tuple1.index(1)) #cout index
# tuple=(2,3,4,65,6,)
# print(max(tuple))
# print(min(tuple))
# tup=input("enter the tuple=").split()
# print(tup)
# sum=0
# for i in tup:
#     sum+=int(i)
# print('sum is',sum)
# to search and find a element in a tuple
# tuple1=(1,3,4,7,8,5,9)
tup=input("enter the tuple=").split()
print(tup)
tup1=tuple(tup) # this is use for converting one to another
print(tup1)
n=int(input("enter the item to be searched="))
i=n
for i in tup:
    if int(i)==n:
        print(n,"is found")
        break
else:
    print(n,"is not fount")



