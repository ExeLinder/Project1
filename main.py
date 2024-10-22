class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def name(self):
        print("My name is " + self.name)
        return self.name

    def age(self):
        print("My age is " + str(self.age))
        return self.age