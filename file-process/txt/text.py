
f = open("test.txt","r")
contents=f.read(100) #read 100 caracters
print(contents)

f.close()

# its better to use context manager to avoid cosing the file after using it 
print("----------------------------------------")

with open("test.txt","r") as f:
    contents=f.readline() #get 1 line
    print(contents)

    contents=f.readline(3) #move to the next line 
    print(contents)

    contents=f.readline(2) #move to the next line and get 2 caract
    print(contents)

    print(f.tell()) #current cracter number




with open("test2.txt","w") as f :
    f.write("hihi")
    f.seek(0)
    f.write("zz")

# we can use 2 context manager to read from and write in other file 

