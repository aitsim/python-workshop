# lambda function is annonyme function with no name 
# In Python, anonymous function means that a function is without 
# a name. As we already know that def keyword is used to define
#  the normal functions and the lambda keyword is used to create
#  anonymous functions. It has the following syntax:
# lambda arguments: expression

def f(x):
    return x*3+1

print(f(3))


# we can do the same job with lambda 

mylist=[2,3,4,5]


newone = [x*3+1 for x in mylist]

print(newone)
#  case 1 

g = lambda x : x*3+1


print(g(3))


# The title() method returns a copy of the string in which first 
# characters of all the words are capitalized.


full_name = lambda x,y: "Hi Mr "+x.strip()+ " "+y.strip().title()


print (full_name("   mohamed","aitsim "))


# every funtion in python has a key funtion  to see just use
#  function name.help()
#key is the function that will be used for sorting 

students=["ahmed abaaqiil","sofia charaf",
          "hemza wanis","haytaam ramzi",
          "oussama imzgane","rachid elbaz"]


students.sort(key = lambda name:name.split(" ")[0].lower())


print(students)

# /Use of lambda() with filter()

# Python code to illustrate 
# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 


# Use of lambda() with map()

# Python code to illustrate  
# map() with lambda()  
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 
