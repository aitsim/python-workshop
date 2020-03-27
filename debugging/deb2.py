import json 
import os

# n execute next line 
# s to get into to the function
# c continue to the next pdb or erreur before 
#  there is other commands for  pdb

dir_path = os.path.dirname(os.path.realpath(__file__))


file_path=os.path.join(dir_path,"test.json")

print(file_path)

# The error clearly says that the file is not to be found. Try the following. 1.
#  make sure that the filename 1.json is available from where you are calling the python interpretor.

def path_to_dict(path):

    with open(path) as json_file:
        json_dict = json.load(json_file)
    return json_dict



def print_values(dict):

    for k,v in dict.items():
        print("{}  :  {}".format(k,v))

import pdb 
pdb.set_trace()
print_values(path_to_dict(file_path))

