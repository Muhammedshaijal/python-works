# polymorphism
# function overloading  ===  it is not support in python
# operator overloading
#
# class Point:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         newa=self.a+other.a
#         newb=self.b+other.b
#         return Point(newa,newb)
#     def __str__(self):
#         return "({0},{1})".format(self.a,self.b)
# p1=Point(2,3)
# p2=Point(3,2)
# print(p1)
# print(p2)
# print(p1+p2)

class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __sub__(self, other):
        newa=self.r-other.r
        newb=self.i-other.i
        return Complex(newa,newb)
    def __str__(self):
        return "({0}+{1}j)".format(self.r,self.i)
c1=Complex(2,3)
c2=Complex(1,4)
print(c1)
print(c2)
print(c1-c2)
