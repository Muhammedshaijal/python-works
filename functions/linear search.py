# # linear search
# lst=input("enter the list=").split()
# key=input("enter the key=")
def linearsearch(lst,key):
    for i in lst:
        if(i==key):
            print("key is found at the position",lst.index(i)+1)
            break
    else:
            print("key is not found at the list")
lst=[1,2,3,4,5]
key=6
linearsearch(lst,key)
