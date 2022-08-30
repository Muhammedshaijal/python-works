class Rectangle:
    def getdata(self,l,b):
         self.__length=l         # int(input('enter the length='))        #.length it is a public data member it will call directly
         self.__breadth=b        #int(input('enter the breadth='))      #__breadth it is the private data member only acces with the function call
    def display(self):
         print('length=',self.__length)
         print('breadth=',self.__breadth)
    def area(self):
         a=self.__length*self.__breadth
         print('area is=',a)
r1=Rectangle()
r1.getdata(10,5)
r1.display()
r1.area()
# print(r1.__length)
# print(r1.__breadth)   #it will show the error