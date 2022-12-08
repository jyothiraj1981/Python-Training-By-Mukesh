#Declaring Variables inside the class
class Myclass:
   a,b=10,20
   def add(self):
     print(self.a+self.b)
   def mul(self):
     print(self.a*self.b)
mc = Myclass()
mc.add()
mc.mul()
