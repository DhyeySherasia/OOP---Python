class Hello1:
    # time has a default value "anything"
    def __init__(self, greetings, time="anything"):
        pass


# NO need to give time
first_hello = Hello1("Greetings")


class Hello2:
    # *args can accept any number of parameters
    # **kwargs can accept parameters with a keyword, here 'name'
    def __init__(self, *args, **kwargs):
        pass


second_hello = Hello2("hey", 30, "anything", name="some_name")


class Hello3:
    def __init__(self, input_name):
        self.name = input_name
        self.age = 10  # static attribute


third_hello = Hello3("arjun")
print(third_hello.name)
print(third_hello.age)
