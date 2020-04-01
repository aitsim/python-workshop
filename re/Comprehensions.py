# def run_script(script, **kwargs):
#     inject_env_vars = partial(
#         re.sub,
#         r'([A-Z0-9_]+)="((?!\$).)*"',
#         lambda match: f'{match.group(1)}=${match.group(1).upper()}' if os.environ.get(match.group(1).upper()) else match.string
#     )
#     with open(script) as file:
#         return BashOperator(
#                task_id='testdag',
#                bash_command='cat {} '.format('\n'.join(map(inject_env_vars, file.readlines()))),
#                dag=dag)

my_list=[1,2,3,4,5,6,7,8,9]
lista=[]

for n in my_list:
    lista.append(n*n)
print(lista)

# using comprehensions
lista2=[n*n for n in my_list]
print(lista2)

# using map function 
def fun(x):
    return x*x

lista3=map(fun,my_list)

for n in lista3:
    print(n)

# print(lista3)
# using lambda 

lista3=map(lambda x:x*x,my_list)

for n in lista3:
    print(n)



# get 2 elements from 2 tabs 

my_list=[]
for i,m in zip("abcd",range(0,4)): 
        my_list.append((i,m))
      
print(my_list)

# using the comp

my_list=[]

new_list=[(x,y) for x,y in zip("abcd",range(0,4))]

print(new_list)


# using to loop

my_list=[]
for x in "abcd":
    for m in range(0,4):
        my_list.append((x,m))

print(my_list)

#  using compre


my_list=[(x,y) for x in "abcd" for y in range(0,4)]

print(my_list)



# exemple 3 with dictionary 

mydict={}

names=["hamza","mehdi","oussama","sara"]
lastnames=["abaaqil","belkihel","aitsihamou","jbaida"]

for i,m in zip(names,lastnames):

    mydict[i]=m

print(mydict)


# using compre



mydict={x:y for x,y in zip(names,lastnames)if x!="sara"}


print(mydict)


# with set()

print("ji")


my_test=[1,1,2,2,3,3]

myset= set()

for m in my_test:
    myset.add(m)
print(myset)


# you should hve a dict so not a array to simulate a set in compre
myset={x for x in my_test}
print(myset)

























