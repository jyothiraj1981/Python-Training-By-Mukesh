try:
	f = open(files.py)
	new_var=old_var
except Exception  as e:
    print("Sorry file doesnot exist")
except Exception as e:
    print("Something went wrong")
else:
     print(f.read())
     f.close()    
finally:
	print("executing finally...")
 