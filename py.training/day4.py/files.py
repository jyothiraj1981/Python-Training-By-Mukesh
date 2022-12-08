
# File Operations 
#Writing data into file 
file = open('D:/jyothika/python_programs/test_write.txt','w')
file.write('Hi iam jyothika\n')
file.write('i love to eat apples\n')
file.write('hello all \n')
file.close()

#Reading entire data from the file
file = open('D:/jyothika/python_programs/test_write.txt','r')
print(file.read())
file.close() 

#Reading specific characters  from the file
file = open('D:/jyothika/python_programs/test_write.txt','r')
print(file.read(10))
file.close()

#Reading all lines as an array
file = open('D:/jyothika/python_programs/test_write.txt','r')
print(file.readlines())
file.close()

#Reading first line of the file
file = open('D:/jyothika/python_programs/test_write.txt','r')
print(file.readline())
file.close()

#Appending Data into the file
file = open('D:/jyothika/python_programs/test_write.txt','a')
file.write('My favorite color is Pink \n')
file.close()