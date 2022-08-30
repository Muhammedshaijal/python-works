#map function
def mul(n):
    return n*n
num=[2,3,4,5,6]
result=map(mul,num) #map(fun,sequence)
print(list(result))

# num=[2,3,4,5,6]
# result=map(lambda n: n*n,num) #using lambda
# print(list(result))

# num1=[1,2,3,4]
# num2=[5,6,7,8]
# result=map(lambda x,y:x+y,num1,num2)
# print(list(result))

# fruits=['apple','orange','mango','banana','jackfruits']
# result=map(len,fruits)
# print(list(result))

# fruits=['apple','orange','mango','banana','jackfruits']
# result=map(list,fruits)
# print(list(result))
#
#
# lst=[2,6,8,5]
# newlst=map(lambda x:x*x,lst)
# print(tuple(newlst))
#
# newlst1=filter(lambda x:x<6,lst)
# print(list(newlst1))
