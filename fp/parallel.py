import multiprocessing
import time
import os

students = [
{"name":"ahmed","born":1992},
{"name":"salim","born":1990},
{"name":"sanae","born":1967},
{"name":"salima","born":2001},
{"name":"houda","born":1997},
{"name":"najat","born":1758}
]

def transform(x):
    # time.sleep()
    print(f'the process {os.getpid()} takes {x["name"]}')
    return {"name":x["name"],"age":2019- x["born"]}

pool = multiprocessing.Pool(processes=1) 
#we can specify the numbers of proccess that will take the job  

start= time.time()

Result=pool.map(transform,students)

end = time.time()

print("the process takes",end-start)

# see tools at 
# https://www.youtube.com/watch?v=0NNV8FDuck8&list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr&index=6
# using threads instead of proceess