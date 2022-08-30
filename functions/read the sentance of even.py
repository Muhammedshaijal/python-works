# word=input("enter the sequence=").split()
# print(word)
# for i in word:
#     if(len(i)%2==0):
#         print(i)


word=input("enter the word=").split()
req=int(input("required="))
print(word)
for i in word:
    if(len(i)>=req):
        print(i)
