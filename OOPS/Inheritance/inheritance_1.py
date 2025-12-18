class Parent:

    #Constructor
    def __init__(self):
        print("Parent class is created")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class is created")

child=Child()