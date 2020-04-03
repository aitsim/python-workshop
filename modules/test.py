from mod import *

import os 

import sys
 
myset=[1,2,3,5,5]



for x in myset:
     print(hi(x))


#  where python check the import path files 


print(sys.path)


#  if y want to execute a file im  different path, 
# you can just add it to sys path list by :

sys.path.append("yourpath")

# or you can jsut add it to bashprofile by
# export PYTHONPATH="MY PATH"


# to get the the file path of some module
# you can jsut do something like 

print(os.__file__)

