# multiple of 3 indicating from n th numbers
n=int(input("enter the limit="))
for i in range(1,n+1,1):
    if i%3==0:
        print(i,"im multiple of 3")
    else:
        print(i)


