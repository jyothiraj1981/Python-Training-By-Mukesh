class Employee:
	def __init__(self,first,last,pay):

	    self.first = first
	    self.last = last
	    self.email = f'{first}.{last}@company.com'
	    self.pay = pay

    def fullname():
        return f'{emp_1.first}{emp_1.last}'


emp_1 = Employee('John','M',600000)
emp_2 = Employee('Kate','F',800000)


print(emp_1.fullname())
print(emp_2.first,emp_2.last,emp_2.email,emp_2.pay)