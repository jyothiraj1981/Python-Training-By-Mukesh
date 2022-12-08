class Employee:
	raise_amt = 1.07
	num_of_emps = 0
    
	def __init__(self,first,last,pay):

	    self.first = first
	    self.last = last
	    self.email = f'{first}.{last}@company.com'
	    self.pay = pay
	    Employee.num_of_emps += 1
    
	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
         
emp_1 = Employee('John','M',600000)
emp_2 = Employee('Kate','F',800000)
emp_1.raise_amt = 1.09

print(Employee.num_of_emps)
print(emp_1.fullname())
print(emp_2.first,emp_2.last,emp_2.email,emp_2.pay)