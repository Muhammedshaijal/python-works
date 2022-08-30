# def sum(a,b):  #a=3,b=4
#     c=a+b
#     return c #it is the return ststemet
# s=sum(3,4)
# avg=s/2
# print("average",avg)


def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
m,n,o,p=calc(3,4)
print('sum is ',m)
print('sub is',n)
print('mul is ',o)
print('div is ',p)
