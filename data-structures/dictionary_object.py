

# dict   d={}
# list   l=[]

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



