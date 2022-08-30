# import functools
# lst=[3,5,1,6,9]
# lst.sort()
# print(lst)
# redu=functools.reduce(lambda x,y:x+y,lst)
# print(redu)


import functools
lst=input('enter the list=').split()
lst1=sorted(list(map(int,lst)))
print(lst1)
lar=functools.reduce(max,lst1)
print(lar,'is the largest')


#
#
# import functools
# lst=input('enter the list=').split()
# lst1=map(int,lst)
# lar=functools.reduce(lambda x,y:x if x>y else y,lst1)
# print(lar,'is large')
