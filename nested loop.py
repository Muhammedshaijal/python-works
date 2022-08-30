# for i in range(4):
#     for j in range(1,4):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n=int(input("enter the number="))#4
x=1
for i in range(0,n):          #(0,4 )
    for k in range(0,n-i-1):  #(4-0-1=3)  here print 3 space in first line
        print(end=" ")
    for j in range(0,i+1):     #(0,0+1=1) here print one *
         print(x,end=" ")
         x=x+1
    print()                       #print in next line

