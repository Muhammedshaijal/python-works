import functools
lst=input("enter the list=").split()
lst1=sorted(list(map(int,lst)))
print(lst1)
even=list(filter(lambda x:x%2==0,lst1))
odd=list(filter(lambda x:x%2!=0,lst1))
print('evenlist=',list(even))
print('odd list=',list(odd))
sum=functools.reduce(lambda x,y:x+y,even)
sum1=functools.reduce(lambda x,y:x+y,odd)
print('sum of even=',sum)
print('sum of odd=',sum1)