# # def data(r,n):
# #     print("roll no:",r)
# #     print("name:",n)
# # data(4,'shaijal')
# # data(n="fayis",r=5)  #key arguements
#
# #student detailes
# def studentdetailes(r,n,d='BCA'):  #here used the default arguments it means the value of department is constsnd
#     print('Roll no:',r)
#     print('name:',n)
#     print('department:',d)
# studentdetailes(1,'shaijal')


#variable length arguments
# def fun1(*num):         #read the numbers the form of tuples used "*" here call the any value passing
#     print(type(num))
#     for i in num:
#         print(i)
# print("call 1")
# fun1(3,45,2,1,3,7)
# print('call 2')
# fun1(4,5,6,87,8)

# def fac(n):
#     f=1
#     for i in range(1,n+1,1):
#         f=f*i
#         print(i)
# fac()


# factors and check the number is perfect
n=int(input("enter the number="))
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if (s==n):
        print(n,"is perfect")
    else:
        print(n,"not perfect")
perfect(n)



