a=int(input("maths="))
b=int(input("chemistry="))
c=int(input("biology="))
if(a<=100 and b<=100 and c<=100):
  t=a+b+c
  p=(t/300)*100
  print(t)
  print(p,"%")
  if(p>=80):
    print("grade A")
  elif(p>=60 and p<=79):
    print("grade B")
  elif(p>=50 and p<=59):
    print("grade C")
  elif(p>=40 and p<=49):
    print("grade D")
  else:
    print("failed")
else:
     print("wrong entry")
