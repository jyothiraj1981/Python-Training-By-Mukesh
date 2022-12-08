def square(i):
   return i*i
def cube(i):
   return i*i*i
def multiple(i):
   return i*i*i*i

list1 = [1,2,3,4]
def a(func,arg_list):
	result =[]
	for i in arg_list:
		result.append(func(i))
	return result
print(a(square,list1))
print(a(cube,list1))
print(a(multiple,list1))




