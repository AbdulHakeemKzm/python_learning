print("Hello, World!")

#open  file
myfile = open("fruits.txt")

#read file
readfile = myfile.read()

#close file
#closefile = myfile.close()

print(readfile)



# method 2 for file operations

with open("files/fruits.txt") as myfile:
	readfile = myfile.read()
	
print(readfile)

#close file
closefile = myfile.close()


# write file 

with open("files/vegetables.txt","w") as myfile:
	myfile.write("Tomato\nOnion\nCarrot")
	
with open("files/vegetables.txt","r") as myfile:
	newfile = myfile.read()
print(newfile)
	
	
	


