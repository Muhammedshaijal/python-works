# accumulate is import from itertools   syntax=accumulator(seq,fun)  by default=its a addition
import itertools

lst=[1,2,3,4]
res=list(itertools.accumulate(lst))
print(res)

lst=[1,2,3,4]
res=list(itertools.accumulate(lst,lambda x,y:x*y))
print(res)
