
try:
    f=open('hi.txt')
    print("from try")
    print(f.read())
    if f.name=='hi.txt':
        print ("hi again")
        raise FileNotFoundError  #atemshi l exception lewla

# specific exception 
except IOError as e:
    print('First!')
except FileNotFoundError :
    print("stooooop")
#  general exception at the bottom of the code 
except Exception as e:
    print(e)
else :
    print("hi babay")

finally:

    # this finnaly will always be executed , we can do many tings like closing db file ....
    print("see y soon ")


print("end of programme")