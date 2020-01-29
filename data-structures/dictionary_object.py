# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning,
# and, it could mean an increase in efficiency or security.



# https://www.w3schools.com/python/python_dictionaries.asp
# dict   d={}
# list   l=[]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


l = {}

l['a'] = 1
l[1] = 2
l['c'] = 3
l['d'] = 4
l['e'] = 5


# keys no sort
for k in l.keys():
    print(k)

# keys tab
print(l.keys())

# len
print(len(l))

# values
for i in l:
    print(l[i])

#list of tuples
print(l.items())


print("--------")


class Med:
    def __init__(self):
        self.son = "aitsim"


instance = Med()
l['obj'] = instance.son

# return list of key value

for key, value in l.items():
    print(key)
    print(value)



