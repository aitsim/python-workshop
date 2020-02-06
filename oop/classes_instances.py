
# useful links
# youtube playlistes : https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# diff between class methods and statioc methods



import datetime


class Employee:
    # class variable
    numEmployees = 0
    salary = 1500

    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        Employee.numEmployees += 1
    # regular methods (pass the instance as a parameter )

    def get_fill_name(self):
        return "my name is {} {}".format(self.first, self.last)

    def get_email(self):
        return self.first + '.' + self.last + '@Company.com'

    # class methods
    # class method receives the class as implicit first argument, just like an instance method receives the instance
    # is bound to the class and not the object of the class.
    # it can modify a class state that would apply across all the instances of the class.
    # We generally use class method to create factory methods.
    # Factory methods return class object ( similar to a constructor ) for different use cases

    @classmethod
    def get_salary(cls, amount):
        cls.salary += amount

    @classmethod
    def from_string(cls, mystring):
        first, last, pay = mystring.split("-")
        return cls(first, last, pay)
    # static method
    # A static method does not receive an implicit first argument.
    # static method cant access or modify it.
    # We generally use static methods to create utility functions

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


a = Employee("med", "aitsihamou", 100)
b = Employee("hamza", "abaaqil", 1000)

print(a.get_fill_name())
print(a.get_email())


print(a.get_fill_name())
print(b.get_email())

print(a.numEmployees)
print(Employee.numEmployees)
print(b.numEmployees)

# get class methods (to modify class variables from //instance or //class)
a.get_salary(10)
print(a.salary)
print(b.salary)
print(Employee.salary)


emp_str_1 = "ahmed-abaaqil-1200"
emp_str_2 = "barik-wissam-1900"
emp_str_3 = "sara-tasila-1800"


emp1 = Employee.from_string(emp_str_1)
emp2 = Employee.from_string(emp_str_3)
emp3 = Employee.from_string(emp_str_3)


print(emp1.get_fill_name())
print(emp1.get_email())

# static methods we cam use them just with the class_name
dd = datetime.date(2019, 5, 6)
aa = datetime.date(2020, 6, 2)
print(Employee.is_workday(dd))
print(Employee.is_workday(aa))
