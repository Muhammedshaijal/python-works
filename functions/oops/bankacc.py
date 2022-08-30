class Bankaccount:
    def getdata(self):
        self.name=input("Name of the depositor=")
        self.acno=int(input("enter the accound number="))
        self.actype=input('accound type=')
        self.amd=int(input("enter the amound in accound="))
    def printdata(self):
        print('NAME OF DEPOSITOR=',self.name)
        print('ACCOUNT NUMBER=',self.acno)
        print('ACCOUNT TYPE=',self.actype)
        print('AMOUND IN THE ACCOUNT=',self.amd)
    def getdeposit(self):
        self.depo=self.amd+int(input('enter the deposite amound='))
        self.printbalance()
    def printbalance(self):
        print("balance amound:",self.depo)
    def withdraw(self):
        withdraw=int(input('enter the withdrawing amount='))
        if self.depo>=withdraw:
            self.depo=self.depo-withdraw
            self.printbalance()
        else:
            print('insificient balance')
    def display(self):
        print('name=',self.name)
        print('account number=',self.acno)
        print('account type=',self.actype)
        print('balance=',self.depo)
obj1=Bankaccount()
obj1.getdata()
# obj1.getdeposit()
# obj1.withdraw()
# obj1.display()
while True:
    print("please enter the option you need")
    print('1.account detailes')
    print("2.deposit amound")
    print('3. balance enquiry')
    print('4.withdraw amound')
    choice=int(input('enter your choice='))
    if choice==1:
        obj1.printdata()
    elif choice==2:
        obj1.getdeposit()
    elif choice==3:
        obj1.printbalance()
    elif choice==4:
        obj1.withdraw()
    else:
        print('invalid choice')
        break

























# class Person:
#     def getdata(self):
#         self.name=input('enter the  name=')
#         self.code=int(input('enter the code='))
# class Account(Person):
#     def getmemberpay(self):
#         self.memberpay=float(input('enter the amount='))
# class Admin(Person):
#     def getexperiance(self):
#         self.experiance=input('enter the year=')
# class Employee(Account,Admin):
#     def getemployeedetailes(self):
#         self.getdata()
#         self.getmemberpay()
#         self.getexperiance()
#     def printemployeedetailes(self):
#         print('name of employee=',self.name)
#         print('code of employee=',self.code)
#         print('member pay=',self.memberpay)
#         print('year of experiance=',self.experiance)
# emp=Employee()
# emp.getemployeedetailes()
# print('employee detailes')
# emp.printemployeedetailes()
#
#

