# multitreading   it is used to split the programes and exicuted parrelly
import threading
import time      #used to knowing tym delays
def calc_square(num):
    print('calculate square')
    for i in num:
        time.sleep(.3)
        print('square=',i*i)
def calc_cube(num):
    print('calculate cube')
    for i in num:
        time.sleep(.3)
        print('cube=',i*i*i)
ar=[2,3,4,5]
t1=threading.Thread(target=calc_square,args=(ar,))
t2=threading.Thread(target=calc_cube,args=(ar,))
t=time.time()   #used to know the time delay
t1.start()
t1.join()
t2.start()
# t1.join()
t2.join()
print('time taken by execution=',time.time()-t)
print('finished execution of threads')
