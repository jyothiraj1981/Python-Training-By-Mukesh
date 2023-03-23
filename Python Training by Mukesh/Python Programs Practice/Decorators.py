def deco_func(orig_func):
	def wrapper_func(*args):
		print('Hello World!')
		return orig_func(*args)

	return wrapper_func
@deco_func
def disp():
	print('This is a disp function')
@deco_func
def disp_info(name,age):
	print(f"disp_info ran with'{name} - '{age}'")
disp_info('John',28)