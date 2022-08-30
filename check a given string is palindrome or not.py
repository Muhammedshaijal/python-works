# str=input("enter the string=")
# str1=str[::-1]
#     # print(str1)
# if(str==str1):
#     print(str1," is palindrome")
# else:
#     print(str,"not a palindrome")
# check the number is palindrome
# n=int(input(("enter the number=")))
# str1=str(n)#here converting a integer to string
# str2=str1[::-1]#reverse the string
# print(str2)
# if(str1==str2):
#     print(str2,"is palindrome")
# else:
#     print(str1,"not a palindrome")
#
#
str="i like programming"
print(str.title()) #this used to chapitalize the first charecter of the words
print(str.capitalize())#used to capitalize the first chsrecter of the string
print(str.upper())#used to capitalize the entire word
str1='HELLO WORLD'
print(str1.lower())#used to lower the words
str2='Hai students'
print(str2.swapcase())#it swap the letters into lower to upper and so on
print(len(str1))#used to count the length including spaces
print(str.isupper())#used to check the str is upper
print(str1.islower())#used to chech the str is lower
str3='@@hello$$'
print(str3.lstrip('@'))#used to cut the left side symbol
print(str3.rstrip('$'))#used to cut the rignt side symbol
print(str3.strip('$@'))#used to cut the both sides
