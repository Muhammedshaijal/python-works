# file ===it is the collection of data  (jpge,pdf,ppt,doc,png)
# file object=open('file_name','mode')
# mode
# r=read
# r+=read,write
# w=write
# w+=read,write
# a=append
# read()==read condent from the file
# tell()==identify the file pointer location
# seek()==used to locate previous location or other locations of file pointer


# f1=open('file','r')
# print('first location=',f1.tell())
# print(f1.read(3))
# print('second location=',f1.tell())
# print(f1.read(3))
# print('third location=',f1.seek(3))
# print(f1.read(3))
# f1.close()

# out side file read
# f1=open(r"C:\Users\HP\OneDrive\Desktop\hey.txt",'r')
# print(f1.read(3))
# f1.close()


# readline()

# f1=open('file','r')
# print(f1.readline())
# f1.close()

# readlines()
# f1=open('file','r')
# print(f1.readlines())
# f1.close()

# f1=open('file','r')
# lst=f1.readlines()
# for i in lst:
#     print(i.strip())
# f1.close()


# write()
# f1=open('file','r+')
# f1.write('hello')
# print(f1.read(5))
# f1.close()

# writelines() ==used to write multiple elements in the lines
f1=open('file','w')
lst=['hello\n','how r you\n','where are you\n']
f1.writelines(lst)
f1.close()

