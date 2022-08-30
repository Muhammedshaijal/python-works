# remove a charecter from specific index of a string

#
# str=input('enter the string=')
# index=int(input('enter the index='))
# str1=str[:index-1]+str[index:]
# print('after removing the specific index=',str1)
#

# find the nth power of the number
def power(n,p):
    if p==0:
        return 1
    return n*power(n,p-1)
n=int(input('enter the 1st number='))
p=int(input('enter the 2nd number= '))
print('power is ',power(n,p))