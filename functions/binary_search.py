def binarysearch(lst,key):
    mid=0
    low=0
    high=len(lst)-1
    while(low<=high):
        mid=(low+high)//2
        if(lst[mid]<key):
            low=mid+1
        elif(lst[mid]>key):
            high=mid-1
        else:
            return mid
        return -1
lst1=input("enter the list=").split()
lst1.sort()
print(lst1)
key=input("enter the key to be searched=")
f=binarysearch(lst1,key)
if(f==-1):
    print("key not found")
else:
    print("key is found",f+1)
