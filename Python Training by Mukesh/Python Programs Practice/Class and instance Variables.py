class Employee():
	raise_amount = 1.08   #Class Variable
	num_of_emp =0

	def __init__(self,first,last,email,pay):
		self.first=first
		self.last=last
		self.email=f"{first}.{last}@company.com"
		self.pay=int(pay)
		Employee.num_of_emp+=1

	def fullname(self):
		return f"{self.first}.{self.last}"

	def apply_raise(self):
		self.pay=int(self.pay*1.08)
                                           

print(Employee.num_of_emp)


emp_1=Employee('John','M','john@company.com',6000) #emp_1 ia an instance variable of class Employee
emp_2=Employee('Jane','J','Jane@company.com',8000) #emp_2 ia an instance variable of class Employee

print(Employee.num_of_emp)

emp_2.raise_amount=1.09
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


#print(Employee.fullname(emp_1))
#print(emp_2.fullname())
#print(emp_1.first)
#print(emp_1.email)
#print(emp_2.last)