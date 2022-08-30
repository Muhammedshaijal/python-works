# single inheritance   one class and sub class

# class Person:
#     def getdata(self):
#         self.voterid=int(input('enter the voter id='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('voter id=',self.voterid)
#         print('name=',self.name)
# class Employee(Person):
#     def getsalary(self):
#         self.salary=int(input('enter the salary='))
#     def printsalary(self):
#         print('salary=',self.salary)
# emp1=Employee()
# emp1.getdata()
# emp1.getsalary()
# emp1.printdata()
# emp1.printsalary()



# overriding===        #it is the function as same as the both parent clas and child class functions are same  and
# class Person:          #
#     def getdata(self):
#         self.voterid=int(input('enter the voter id='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('voter id=',self.voterid)
#         print('name=',self.name)
# class Employee(Person):
#     def getdata(self):
#         self.salary=int(input('enter the salary='))
#     def printdata(self):
#         print('salary=',self.salary)
# emp1=Employee()
# emp1.getdata()
# emp1.printdata()



# super class ()
# class Person:
#     def getdata(self):
#         self.voterid=int(input('enter the voter id='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('voter id=',self.voterid)
#         print('name=',self.name)
# class Employee(Person):
#     def getdata(self):
#         super().getdata()
#         self.salary=int(input('enter the salary='))
#     def printdata(self):
#         super().printdata()
#         print('salary=',self.salary)
# emp1=Employee()
# emp1.getdata()
# emp1.printdata()


# using constuctor
# class Person:
#     def __init__(self):
#         self.voterid=int(input('enter the voter id='))
#         self.name=input('enter the name=')
#     def printdata(self):
#         print('voter id=',self.voterid)
#         print('name=',self.name)
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.salary=int(input('enter the salary='))
#     def printdata(self):
#         super().printdata()
#         print('salary=',self.salary)
# emp1=Employee()
# emp1.printdata()


# using parameters v(voter id),n(name),s(salary)
class Person:
    def __init__(self,v,n):
        self.voterid=v
        self.name=n
    def printdata(self):
        print('voterid=',self.voterid)
        print('name=',self.name)
class Employee(Person):
    def __init__(self,v,n,s):
     super().__init__(v,n)
     self.salary=s
    def printdata(self):
        super().printdata()
        print('salary=',self.salary)
emp1=Employee(2,'anu',3000)
emp1.printdata()
