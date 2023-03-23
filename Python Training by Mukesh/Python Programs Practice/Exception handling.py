#try:
#	f=open('demo1.txt')
#	x =y
#except FileNotFoundError:
#	print('Sorry,This file does not exist')
#except Exception:
#	print('Sorry,Something went Wrong')



try:
	f=open('demo1.txt')
	#x =y
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print("Executed finally...")