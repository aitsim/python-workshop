# 2 classes inheritance from Employee

from classes_instances import Employee


class Developer(Employee):
    salary = 1990

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)   #bhal Employee.__init__(self,first....)
        self.language = language

a = Developer("med", "aitsihamou", 100,"c")
# b = Developer("hamza", "abaaqil", 1000)


print("hi")

a.get_salary(20)
print(a.salary)


class Manager(Employee):

    def __init__(self,first,last,pay,employes=None):
        super().__init__(first,last,pay)
        if employes == None:
            self.employes=[]
        self.employes=employes

    def add_emp(self,emp):
        if emp not in self.employes:
            self.employes.append(emp)

    def remove_emp(self,emp):
        if emp in self.employes:
            self.employes.remove(emp)

    def get_all_emp(self):
        for emp in self.employes:
            print(emp.get_fill_name())


s = Employee("med", "aitsihamou", 100)
z = Employee("hamza", "abaaqil", 1000)



mg1 = Manager("salim", "hammoumi",100,[z,s])

print(mg1.get_fill_name())

mg1.get_all_emp()






