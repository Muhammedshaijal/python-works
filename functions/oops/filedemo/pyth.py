# f=open('file','r')
# f2=open('file2','w')
# lst=f.readlines()
# f2.writelines(lst)
# f.close()
# f2.close()
#
#

#number of words  with unique words

# f2=open('file2','r')
# string=set(f2.read().split())
# print(string)
# c=0
# for i in string:
#     c=c+1
# print(c)

# number of words count

# dict={}
# dict['hello']=1
# dict['hello']+=1
# print(dict)
# def wordcount()

def wordcount(lst):
    dict={}
    for i in lst:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for k,v in dict.items():
        print(k,':',v)
    # print(dict)
f2=open('file2','r')
string=f2.read().split()
wordcount(string)




