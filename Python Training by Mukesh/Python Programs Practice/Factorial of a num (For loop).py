#Factorial of a num using for loop
factorial = 1
num =5 
if num<0 :
	print("Factorial does not exist for negative numbers")
elif num==0:
	print("Factorial of 0 is 1")
else:
	for i in range(1,num+1):
		factorial = factorial*i 
	print("Factorial of a num",num, "is",factorial)



#factorial of a number using recursive method
def factorial(n):
	if(n==0 or n==1):
		return 1
	else:
		return n * factorial(n-1)
num =10
print("factorial of ",num,  "is", factorial(num))