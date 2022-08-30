# variable length argument *args
# def var_length(*arg):
#     print(type(arg))
#     for i in arg:
#         print(i)
# var_length(20,30)
# var_length(2,3,4,5)



 # variable length arguments **kargs====keyword arguments
#
# def fun(**karg):
#     print(type(karg))
#     for k,v in karg.items():
#         print(k,':',v)
# fun(name='anu',cls='bca')



# reguler expressions   match,search,findall,sub
# import re
# str='python programming'
# result=re.search('python',str)                        #re.search('pattern',str)
# if result:
#     print('pattern exist')
# else:
#     print('pattern not exist')



# using match
#
# import re
# str='python programming is fun'
# result=re.match('fun',str)                        #re.search('pattern',str)
# if result:
#     print('pattern exist')
# else:
#     print('pattern not exist')

# its only give the out put of the first word only. its not compile the entire lines so out put is not exist

# using findall
# import re
# str1='123-33-4 safyf 2'
# new=re.findall('\d',str1)   #\d used to find and match all digits  and \D is used to does not contain adigit
# print(new)
# new1=re.sub('\d','$',str1)    #used to substitite
# print(new1)
#



# password
#




import re

password=input('enter the password=')
if (len(password)<=6 or len(password)>=16):
    print('invalid password')
elif not re.search('[a-z]',password):
    print('invalid password')
elif not re.search('[A-Z]',password):
    print('invalid password')
elif not re.search('[0-9]',password):
    print('invalid password')
elif not re.search('[@$&!]',password):
    print('invalid password')
else:
    print('valid password')











