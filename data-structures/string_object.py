

s = "hi my name is mohamed"


for i in range(0, s.__len__()):
    print(s[i])


print("-----")
# last element
print(s[-1])



# concat
a = "abc"
b = 123
print((a+b.__str__()))
print(a+str(b))

print(a.isdigit())
# .
# .
# there is multiple string methods



test = open("loren.txt","r")

# return string object
test2=test.read()

print(len(test2))

test3=test2.split(".")
print(test3)
for i in test3:
    print(i)


# list https://www.w3schools.com/python/python_lists.asp

list=["tete","ueuueu","uhauhua"]

for i in list:
    print(i)




list.append(1)


print(list)


tab=[10,2,4.5]
tab[0]=2



for i in tab:
    print(i)



#  get elements from 2 tabs


tab1=[2,3,5,6,7]
tab2=[6,66,6,6,6]


for a, b in zip(tab1,tab2):
    print("{0}.{1}".format(a, b))
    print("%d,%d"%(a, b)) #d integer ...

#  we can delete an element by using del function   del a[0
#  we can drop last element by a.pop(), get element by index a.index(i) .... sort()

#  try tp use catch exception
try:
    print(3)
except:
    print("non exsire")

def test(x):
    return x*3


#  we can return function inside  array


tabb=[1,2,3,4,5,6]

tabaa=[test(x) for x in tabb]


print(tabaa)


#  list object







