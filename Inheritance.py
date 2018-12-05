
g = 0


class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        global g
        g += 1
        self.staffnum = g


class Employee(Person):

    def __init__(self, first, last):
        super(Employee, self).__init__(first, last)

    def __str__(self):
        return "[" + str(self.staffnum) + "] " + self.firstname + " " + self.lastname


x = Employee("Marge", "Simpson")
y = Employee("Homer", "Simpson")

print(x)
print(y)