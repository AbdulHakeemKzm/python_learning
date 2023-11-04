# standard modules with eg:

'''
import time
import os

while True:
	if os.path.exists("files/vegetables.txt"):
		with open("files/vegetables.txt")as file:
			print(file.read())
	else:
		print("file does not exists")
	time.sleep(5)

'''

import time
import os
import pandas

while True:
	if os.path.exists("files/temps.csv"):
		data  = pandas.read_csv("files/temps.csv")
		print(data.mean())
	else:
		print("file does not exists")
	time.sleep(10)
	
	

