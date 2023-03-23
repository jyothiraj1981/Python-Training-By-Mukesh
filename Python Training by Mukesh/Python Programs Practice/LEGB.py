#def outer():
#	x ='outer x'
#	print(x)
#outer()

x ='global x'        #global 
def outer():
	x = 'outer x'    #Enclosing
	def inner():
		x = 'inner x' #Local
		print(x)
		inner()
	print(x)
outer()
