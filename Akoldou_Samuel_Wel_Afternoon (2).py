class Error:  
   def __init__(self, argument):  
      self.arguments = argument  
try:  
    div = 20 // 0    
    print( div )  
# this block will handle the exception raised  
except ZeroDivisionError:  
    print( "the result can not be executed " )  
# this will always be executed no matter exception is raised or not  
finally:  
    print('Iam always executed reqardless of the circumstance')

 # File handling exception


file = open('tycoon.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)

import os

def my_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: failed to create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: failed to read file " + filename)
def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: failed to  rename the file, try again " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error : it has not been deleted, try again " + filename)


if __name__ == '__main__':
	filename = "samuel.txt"
	new_filename = "akoldou.txt"

	my_file(filename)
	read_file(filename)
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)
  

