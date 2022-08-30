# a function call it self
# factorial of a number
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# sum of n natural numbers
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(10))







# lambda function(anonymous function)
# sq=lambda n:n*n  #squre of a number     syntax= s=lambda arg1,arg2..:expression
#                                                 # print(s())
# print(sq(2))
# # sum of numbers
# sum=lambda a,b:a+b
# print(sum(2,3))
# sum=lambda a,b,c:a+b+c
# print(sum(2,3,4))
# mul=lambda a,b:a*b
# print(mul(5,5))
# qu=lambda a:a*a*a
# print(qu(3))

# lambda using function
# find largest among 3 numbers
# def large(a,b,c):
#     if(a>b and a>c):
#         print(a,"is large")
#     elif(b>a and b>c):
#         print(b,"is larger")
#     else:
#         print(c,"is large")
# print(large(4,3,2))

# using function return list of even numbers
# n=int(input('enter the limit='))
# def evenfun(lst):
#     evenlist=[]
#     for i in lst:
#         if(i%2==0):
#             evenlist.append(i)
#     print(evenlist)
# lst=[1,2,3,4,5,6,7,8,9]
# evenfun(lst)