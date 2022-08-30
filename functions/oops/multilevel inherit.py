# multilevel inheritance
# a-b-c

#
# class Student:
#     def getdata(self):
#         self.rollno=int(input('enter the rollno='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('rollno=',self.rollno)
#         print('name=',self.name)
# class Mark(Student):
#     def getmark(self):
#         self.mark=int(input('enter the mark='))
#     def printmark(self):
#         print('mark=',self.mark)
# class Grade(Mark):
#     def calculategrade(self):
#         p=self.mark/500*100
#         if(p>80):
#             print('grade A')
#         elif(p>70):
#             print('grade B')
#         elif(p>60):
#             print('grade c')
#         elif(p>50):
#             print('grade d')
#         else:
#             print('failed')
#
#
# s1=Grade()
# s1.getdata()
# s1.getmark()
# s1.printdata()
# s1.printmark()
# s1.calculategrade()


# using init
# class Student:
#     def __init__(self):
#         self.rollno=int(input('enter the rollno='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('rollno=',self.rollno)
#         print('name=',self.name)
# class Mark(Student):
#     def __init__(self):
#         Student.__init__(self)
#         self.mark=int(input('enter the mark='))
#     def printmark(self):
#         print('mark=',self.mark)
# class Grade(Mark):
#     def __init__(self):
#         Mark.__init__(self)
#     def calculate(self):
#         p=self.mark/500*100
#         if(p>80):
#             print('grade A')
#         elif(p>70):
#             print('grade B')
#         elif(p>60):
#             print('grade c')
#         elif(p>50):
#             print('grade d')
#         else:
#             print('failed')
# s1=Grade()
# s1.printdata()
# s1.printmark()
# s1.calculate()

# using parameters
class Student:
    def __init__(self,r,n):
        self.rollno=r           #int(input('enter the rollno='))
        self.name=n             #input('enter the name=')
    def printdata(self):
        print('rollno=',self.rollno)
        print('name=',self.name)
class Mark(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.mark=m        #int(input('enter the mark='))
    def printmark(self):
        print('mark=',self.mark)
class Grade(Mark):
    def __init__(self,r,n,m):
        Mark.__init__(self,r,n,m)
    def calculate(self):
        p=self.mark/500*100
        if(p>80):
            print('grade A')
        elif(p>70):
            print('grade B')
        elif(p>60):
            print('grade c')
        elif(p>50):
            print('grade d')
        else:
            print('failed')
s1=Grade(1,'anu',4000)
s1.printdata()
s1.printmark()
s1.calculate()

