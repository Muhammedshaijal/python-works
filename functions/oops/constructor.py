# constructor it is the function used to initialize data members
class Rectangle:
     def __init__(self,l,b):
         self.length=l         # int(input('enter the length='))
         self.breadth=b        #int(input('enter the breadth='))
     def display(self):
         print('length=',self.length)
         print('breadth=',self.breadth)
     def area(self):
         a=self.length*self.breadth
         print('area is=',a)
r1=Rectangle(10,5)
r1.display()
r1.area()
r2=Rectangle(20,5)
r2.display()
