# find to she a word in the file
# import re
# file=open('f1','r')
# txt=file.readlines()
# for i in txt:
#     result=re.search('she',i)
#     if(result):
#         print(i)
#

#  r is used to identify the regular expression pattern '\bs used the space denoted.'.' and
# import re
# file=open('f1','r')
# txt=file.readlines()
# for i in txt:
#     result=re.search(r'\bs.e\b',i)
#     if(result):
#         print(i)
#used \wwordchrecter'*e'denotesanycharecter and combinationbetweenthes and e
import re
file=open('f1','r')
txt=file.readlines()
for i in txt:
    result=re.search(r'\bs\w*e\b',i)
    if(result):
        print(i)