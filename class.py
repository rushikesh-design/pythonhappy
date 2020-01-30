class Employee:
	company = "Vinsys"
	def calculatetax2():
		print("calculatetax2 Called.......")
	def __init__(self):
		print("Constructor Called.......")
	def calculate_tax(self):
		print("calculate_tax Called.......")
	def __del__(self):
		print("Destructor Called.......")
	def __str__(self):
		return "i love python"
emp=Employee()
Employee.calculatetax2()
emp.company
print(emp)