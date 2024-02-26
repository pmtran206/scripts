
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"
    
    def myfunc(self):
        print("Person is named: " + self.name)


p1 = Person("John", 45)

print(p1)

p1.myfunc()