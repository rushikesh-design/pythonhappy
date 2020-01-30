def myfn():
	a=10
	yield a
	print("doing work")
	print("doing more work")

	a=20
	yield a

	print("doing work")
	print("doing more work")
	
	a=30
	yield a

#print(myfn())
