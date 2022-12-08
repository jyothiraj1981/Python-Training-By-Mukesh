#To invoke parent class variables
class A:
    a,b=10,20
class B(A):
    i,j=100,200
    def m1(self,x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)
b1=B()
b1.m1(1,2)
