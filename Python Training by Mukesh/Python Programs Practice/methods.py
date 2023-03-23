class Employee():
	raise_amount = 1.08   

	def __init__(self,first,last,email,pay):
		self.first=first
		self.last=last
		self.email=f"{first}.{last}@company.com"
		self.pay=int(pay)
		

	def fullname(self):
		return f"{self.first}.{self.last}"

	def apply_raise(self):
		self.pay=int(self.pay*1.08)

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount=amount

	@classmethod
	def from_str(cls, emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True


                                           

emp_1=Employee('John','M','john@company.com',6000) #emp_1 ia an instance variable of class Employee
emp_2=Employee('Jane','J','Jane@company.com',8000) #emp_2 ia an instance variable of class Employee

import datetime
my_date=datetime.date(2023,11,3)
print(Employee.is_workday(my_date))

#new_emp_str = 'Tom-L-7000'
#new_emp=Employee.from_str(new_emp_str)
#print(new_emp.first)
#first,last,pay =emp_str.split('-')
#new_emp= Employee(first,last,pay)
#Employee.set_raise_amt(1.09)
#print(emp_1.raise_amount)
