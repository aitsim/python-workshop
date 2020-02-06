# Property Decorators - Getters, Setters, and Deleters\
# Getter and Setter in Python
# Getters and Setters in python are often used when:
#
# We use getters & setters to add validation logic around getting and setting a value.
# To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

#-----
#The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code

#-----
# Python program showing a
# use of property() function

class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property  #get_age
    def age(self):
        print("getter method called")
        return self._age

        # a setter function

    @age.setter  #set_age
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 19

print(mark.age)
