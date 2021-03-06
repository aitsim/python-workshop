# __name__ (A Special variable) in Python
# Since there is no main() function in Python,
#  when the command to run a python program is
#   given to the interpreter, the code that is 
#   at level 0 indentation is to be executed. However,
#    before doing that, it will define a few special 
#    variables. __name__ is one such special variable.
#     If the source file is executed as the main program,
# 	 the interpreter sets the __name__ variable to have 
# 	 a value “__main__”. If this file is being imported 
# 	 from another module, __name__ will be set to the 
# 	 module’s name.

# File1.py 


print ("File1 __name__ = %s" %__name__ )

if __name__ == "__main__": 
	print("File1 is being run directly")
else: 
	print("File1 is being imported")
