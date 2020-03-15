# map() function returns a map object(which is an iterator) of the results 
# after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax :
# map(fun, iter)

# NOTE : You can pass one or more iterable to the map() function.

import pprint

def fun(x):
    return x['name'], 2020-x['born']


mylist=[{"name":'mohamed',"born":1996},
        {"name":"sami","born":2007}
        ]
new_list = map(fun,mylist)

my_second= [{"name":x["name"],"age":2020-x["born"]} for x in mylist]

my_third=map(lambda x: {"name":x["name"],"age":2020-x["born"]}, mylist)


print(new_list)
print("-------")
print(my_second)

print("-----")


print(my_third)