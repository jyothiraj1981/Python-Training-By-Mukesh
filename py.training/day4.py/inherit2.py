#to invoke all variables with same name 
a,b = 100,200  #global variables
class A:
    a,b=10,20  #parent class variables
class B(A):
    a,b=15,25  # Child class variables
    def m1(self,a,b):                        #local variables
        print(a+b)                           # accessing local variables
        print(self.a+self.b)                 #accessing child class variables
        print(super().a + super().b)         # accessing Parent class variables
        print(globals()['a']+globals()['b'])  #accessing global variables
b1=B()
b1.m1(1,2)
