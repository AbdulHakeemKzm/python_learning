#print("Hello, World!")

def divide(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		return "Zero division not allowed"

print(divide(1,0))
print("end")
