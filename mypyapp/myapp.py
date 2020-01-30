"""
DocumentString
"""

list_of_users = ["Nilesh","Ramesh","Satish","abhijit"]

for user in list_of_users:
	print(user)   

print("-------globals-------")
print(globals())


def do_something():
	print("doing somethig")
	return 10394

def cal_tax(a):
	print(a)

def manage_user(b,p,a=10):
	print(a)

do_something()
cal_tax(10)

def my_sample_fn(a):
	a()

def my_callback():
	print("i am callback")

my_sample_fn(my_callback)

def my_another_fn():
	def some_other_fn():
		print("other fn")
	return some_other_fn

my_another_fn()()

def some_fn_with_params(a,b=30):
	print(a)
	print(b)

some_fn_with_params(a=10,b=20)

my_range = range(1,100,25)
for i in my_range:
	print(i)

