class Test:
    name = "Jan"

    def greet(self):
        print("czesc")

#a = Test()

#a.greet()

class Test_1:
    def __init__(self, greeting : str):
        self.greeting = greeting
        print(self.greeting)

a_1 = Test_1("cześć")

#a.greet()

a = Test()

print(a.name)




