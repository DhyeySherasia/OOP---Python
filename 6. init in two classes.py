class Parent1:
    def __init__(self, name):
        print("Parent1 __init__", name)


class Parent2:
    def __init__(self):
        print("Parent2 __init__")


class Child(Parent1, Parent2):
    def __init__(self):
        print("Child __init__")

        # This format is used to call __init__ of parent class
        # super().__init__("input_name")  # can also give input arguments
        Parent1.__init__(self, "input_name")
        Parent2.__init__(self)


child_object = Child()
print(Child.__mro__)
