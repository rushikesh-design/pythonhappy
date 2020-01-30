

def check_null(obj):
	if obj is None:
		return True
		print("1T")
	else:
		return False
		print("1F")

def check_empty(obj):
	if check_null(obj):
		return True
		print("2T")
	else:	
		if len(obj) == 0:
			return True
			print("2TT")
		else :
			return False
			print("2F")