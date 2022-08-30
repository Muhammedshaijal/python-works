# multiple inhertance
# a->c <-b
class Mark:
    def getmark(self):
        self.mark=int(input('enter the mark='))
    def printmark(self):
        print('mark=',self.mark)
class Gracemark:
    def getgmark(self):
        self.gmark=int(input('enter the Gmark='))
    def printgmark(self):
        print('Gmark=',self.gmark)
class Grade(Mark,Gracemark):
    def calculate(self):
        tottal=self.mark+self.gmark
        p=tottal/500*100
        if (p > 80):
            print('grade A')
        elif (p > 70):
            print('grade B')
        elif (p > 60):
            print('grade c')
        elif (p > 50):
            print('grade d')
        else:
            print('failed')
g1=Grade()
g1.getmark()
g1.getgmark()
g1.printmark()
g1.printgmark()
g1.calculate()