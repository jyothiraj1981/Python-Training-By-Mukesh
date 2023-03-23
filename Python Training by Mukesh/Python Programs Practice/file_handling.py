#Reading a File
#with open('demo1.txt','r') as f:
#	content = f.read()
#	print(content)


#Reading a file using readline()
#with open('demo1.txt','r')as f:
#	content=f.readline()
#	print(content)
#	content = f.readline()
#	print(content)
#	content = f.readline()
#	print(content)
#	content = f.readline()
#	print(content)

#Reading a file using for loop
#with open('demo1.txt','r') as f:
#	for line in f:
#		print(line,end='')


#Writing a file
#Creates a new file with new_demo
#with open('new_demo.txt','w')as f:
#	pass


#Writing inside the file created
#with open('new_demo.txt','w')as f:
#	f.write('New_line')
#	f.seek(0)
#	f.write('demo')

#  Copy a File
#with open('demo1.txt','r')as rf:
#	with open('demo_2.txt','w')as wf:
#		for line in rf:
#			wf.write(line)

# Working on csv files

#import csv
#with open('info.csv','r')as csv_file:
	#csv_reader=csv.reader(csv_file)
	#for line in (csv_reader):
	#	print(line)

#Copying a CSV file

import csv

with open('info.csv','r')as csv_file:
	csv_reader = csv.reader(csv_file)
	with open('new_info.csv','w')as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t')
		for line in csv_reader:
			csv_writer.writerow(line)


#Reading the data in the form of Dictionary
import csv

with open('info.csv','r')as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for line in csv_reader:
		print(line)
