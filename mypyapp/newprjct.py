
def airport(filename):
	file = open(file = filename,mode = "rt",encoding="utf-8")
	line = file.readline()
	SMALL_AIRPORT = 0
	LARGE_AIRPORT = 0
	while line:
		line = line.replace("\"","")
		data = line.split(",")
		if data[2] == "small_airport":
			SMALL_AIRPORT = SMALL_AIRPORT + 1
		elif data[2] == "large_airport":
			LARGE_AIRPORT = LARGE_AIRPORT + 1
		else:
			pass
	
		line = file.readline() 
	print("SMALL_AIRPORT",SMALL_AIRPORT)
	print("LARGE_AIRPORT",LARGE_AIRPORT)

airport("C:/airports.csv")


username = input("Enter username :")
password = input("Enter password")
print("username{} and password{}".format(username,password))


