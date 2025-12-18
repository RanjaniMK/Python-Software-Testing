class Parent:

    #Constructor
    def __init__(self):
        print("Parent class is created")


    #method
    def speak(self):
        print("Parent is speaking")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class is created")

    #method
    def speak(self):

        super().speak()
        print("Child is speaking")

child=Child()

print("Break")

child.speak()