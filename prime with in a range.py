l=int(input("enter the lower limit="))
u=int(input("enter the upper limit="))
for i in range(l,u):
    for j in range(2,i-1):
        if(i%j==0):
            break
    else:
        print(i,end=" ")


#menu
#add
#sub
#mul
#devi
#exit
#enter your choice=
