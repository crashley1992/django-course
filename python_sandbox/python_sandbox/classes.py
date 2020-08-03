# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name}'

    def has_birthday(self):
        self.age += 1



# init user object
ashley = User('Ashley Clarke', 'email@email.com', 27)

# edit propery
ashley.age = 28

# gets name
print(ashley.name)

# updated age
# print(ashley.age)

# print(ashley.has_birthday())
# print(ashley.age)


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I owe a balance of {self.balance}'


# init customer
john = Customer('John Doe', 'john@gmail.com', 40)
print(john.name)

john.set_balance(500)
print(john.greeting())